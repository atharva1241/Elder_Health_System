# vitals_module.py

import random


# These are the normal and critical values used to compare readings.
THRESHOLDS = {
    "heart_rate": {
        "normal_min": 60,
        "normal_max": 100,
        "warning_max": 120,
        "critical_low": 40,
        "critical_high": 120,
    },

    "temperature_c": {
        "normal_min": 36.1,
        "normal_max": 37.2,
        "warning_max": 38.9,
        "critical_high": 39.0,
    },

    "spo2": {
        "normal_min": 94,
        "warning_min": 90,
        "critical_min": 90,
    },
}


def simulate_vitals(mode="normal"):
    """
    Generate simulated heart rate, temperature and SpO2 values.
    """

    if mode == "normal":
        # Normal mode
        hr = random.randint(65, 85)
        temp = round(random.uniform(36.4, 36.9), 1)
        spo2 = random.randint(95, 99)

    elif mode == "random":
        # Random mode
        hr = random.randint(50, 140)
        temp = round(random.uniform(35.5, 40.5), 1)
        spo2 = random.randint(85, 99)

    elif mode == "danger":
        # Danger mode
        hr = random.choice([
            random.randint(121, 160),
            random.randint(20, 39)
        ])
        temp = round(random.uniform(39.0, 41.0), 1)
        spo2 = random.randint(80, 89)

    elif mode == "edge":
        # Edge-case mode
        hr = random.choice([100, 120, 40])
        temp = random.choice([37.3, 38.9, 39.0])
        spo2 = random.choice([93, 90, 89])

    else:
        # Fallback mode
        hr = random.randint(30, 160)
        temp = round(random.uniform(34.0, 41.5), 1)
        spo2 = random.randint(70, 100)

    return hr, temp, spo2


def check_vitals(hr, temp_c, spo2):
    """
    Compare vital readings with the predefined thresholds.
    Returns status and a note.
    """

    notes = []
    status = "Normal"

    # Check heart rate
    thr = THRESHOLDS["heart_rate"]

    if hr is not None:
        if hr < thr["critical_low"] or hr > thr["critical_high"]:
            status = "Critical"
            notes.append(f"HR critical ({hr} bpm)")

        elif hr > thr["warning_max"]:
            status = "Warning"
            notes.append(f"HR high ({hr} bpm)")

    # Check temperature
    tthr = THRESHOLDS["temperature_c"]

    if temp_c is not None:
        if temp_c >= tthr["critical_high"]:
            status = "Critical"
            notes.append(f"Temp critical ({temp_c}°C)")

        elif temp_c > tthr["warning_max"]:
            status = "Warning"
            notes.append(f"Temp high ({temp_c}°C)")

    # Check SpO2
    sthr = THRESHOLDS["spo2"]

    if spo2 is not None:
        if spo2 < sthr["critical_min"]:
            status = "Critical"
            notes.append(f"SpO2 critical ({spo2}%)")

        elif spo2 < sthr["warning_min"]:
            status = "Warning"
            notes.append(f"SpO2 low ({spo2}%)")

    note_str = (
        "; ".join(notes)
        if notes
        else "All vitals within normal range"
    )

    return status, note_str
