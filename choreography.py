import numpy as np
from pose_library import get_pose, SEQUENCE, HALFBEAT_SEQUENCE

CHORUS_START = 67.0
CHORUS_END = 83.5
HALFBEAT_PROB = 0.0

# function to align poses with beats
def build_cue_list(beat_times, HALFBEAT_PROB):
    cue_list = []

    # change this hardcoded time value later
    for i, beat_time in enumerate(beat_times[:224]):
        pose_name = SEQUENCE[i] if i < len(SEQUENCE) else "arms_wide"
        cue_list.append({
            "time": float(beat_time),
            "pose": pose_name,
            "type": "beat"
        })
        print(f"beat {i+1:2d}  t={beat_time:.3f}s: {pose_name}")

        if i < len(beat_times) - 1 and CHORUS_START <= beat_time <= CHORUS_END and np.random.random() < HALFBEAT_PROB:
            halfbeat_time = (beat_times[i] + beat_times[i + 1]) / 2.0
            halfbeat_pose = HALFBEAT_SEQUENCE[i % len(HALFBEAT_SEQUENCE)]
            cue_list.append({
                "time": float(halfbeat_time),
                "pose": halfbeat_pose,
                "type": "halfbeat",
            })
            print(f"  halfbeat  t={halfbeat_time:.3f}s: {halfbeat_pose}")

    return cue_list


def get_current_cue(cue_list, current_time):
    current_cue = None
    for cue in cue_list:
        if cue["time"] <= current_time:
            current_cue = cue
        else:
            break
    return current_cue