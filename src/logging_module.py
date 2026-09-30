# logging_module.py

import csv
import os
from datetime import datetime


LOG_TO_CSV = True
CSV_FILENAME = "vitals_log.csv"


def ensure_csv_header(path):
    """
    Create the CSV file and add the header if it does not exist.
    """

    if not LOG_TO_CSV:
        return

    if not os.path.exists(path):
        with open(path, mode="w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "timestamp",
                "heart_rate_bpm",
                "temperature_c",
                "spo2_percent",
                "status",
                "note"
            ])


def log_reading(
    path,
    hr,
    temp_c,
    spo2,
    status,
    note=""
):
    """
    Store one vital-sign reading in the CSV file.
    """

    if not LOG_TO_CSV:
        return

    with open(path, mode="a", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            hr if hr is not None else "",
            f"{temp_c:.1f}" if temp_c is not None else "",
            spo2 if spo2 is not None else "",
            status,
            note,
        ])
