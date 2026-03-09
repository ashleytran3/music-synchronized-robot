import time
import numpy as np
import pygame

from env_setup import make_env
from beat_detection import detect_downbeats
from choreography import build_cue_list, get_current_cue
from pose_library import get_pose


def start_audio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    print(f"Playing: {audio_path}")
    return time.time()


def stop_audio():
    pygame.mixer.music.stop()
    pygame.mixer.quit()


def run(audio_path="./assets/uptown_funk.mp3", play_audio=True):
    # beat detection
    bpm, beat_times, downbeat_times = detect_downbeats(audio_path)
    cue_list = build_cue_list(beat_times)

    # environment
    env = make_env()
    obs = env.reset()

    last_pose = "neutral"
    current_action = get_pose("neutral")

    if play_audio:
        start_time = start_audio(audio_path)
    else:
        start_time = time.time()
        print("Running without audio")

    try:
        while True:
            current_time = time.time() - start_time

            if current_time > 6.0:
                print("Done!")
                break

            cue = get_current_cue(cue_list, current_time)
            if cue and cue["pose"] != last_pose:
                print(f"t={current_time:.2f}s  beat: {cue['pose']}")
                current_action = get_pose(cue["pose"])
                last_pose = cue["pose"]

            obs, _, _, _ = env.step(current_action)
            env.render()

    except KeyboardInterrupt:
        print("Stopped by user")

    finally:
        stop_audio()
        env.close()


if __name__ == "__main__":
    run(
        audio_path="./assets/uptown_funk.mp3",
        play_audio=True,
    )