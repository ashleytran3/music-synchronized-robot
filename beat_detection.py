import numpy as np
import librosa
import sys

def detect_beats(audio_path):
    print(f"Loading audio: {audio_path}")
    y, sample_rate = librosa.load(audio_path)

    print("Detecting beats...")
    bpm, beat_frames = librosa.beat.beat_track(y=y, sr=sample_rate)
    bpm = float(np.squeeze(bpm))

    # Convert beat frame indices to timestamps in seconds
    beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)

    return float(bpm), beat_times


def detect_downbeats(audio_path):
    bpm, beat_times = detect_beats(audio_path)

    # assuming 4/4 time signature for uptown funk
    downbeat_times = beat_times[::4]

    print(f"Downbeats: {len(downbeat_times)}")

    return bpm, beat_times, downbeat_times


def get_beat_interval(bpm):
    return 60.0 / bpm


if __name__ == "__main__":
    # set uptown funk as default arg
    audio_path = sys.argv[1] if len(sys.argv) > 1 else "./assets/uptown_funk.mp3"

    bpm, beat_times, downbeat_times = detect_downbeats(audio_path)

    print("\n── Summary ───────────────────────────────────────")
    print(f"BPM            : {bpm:.2f}")
    print(f"Beat interval  : {get_beat_interval(bpm):.4f} seconds")
    print(f"Total beats    : {len(beat_times)}")
    print(f"Total downbeats: {len(downbeat_times)}")
    print(f"All beat times : {np.round(beat_times, 3).tolist()}")