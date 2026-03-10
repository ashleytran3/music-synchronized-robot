import numpy as np
from pose_library import get_pose, SEQUENCE


def build_cue_list(beat_times):
    cue_list = []

    # change this hardcoded time value later
    for i, beat_time in enumerate(beat_times[:36]):
        pose_name = SEQUENCE[i]
        cue_list.append({
            "time": float(beat_time),
            "pose": pose_name,
        })
        print(f"beat {i+1:2d}  t={beat_time:.3f}s: {pose_name}")

    return cue_list


def get_current_cue(cue_list, current_time):
    current_cue = None
    for cue in cue_list:
        if cue["time"] <= current_time:
            current_cue = cue
        else:
            break
    return current_cue