# alert_module.py

from datetime import datetime

from logging_module import (
    log_reading,
    CSV_FILENAME
)


# Emergency contact information.
EMERGENCY_CONTACT = {
    "ambulance_number": "102",
    "caregiver_name": "Family",
    "caregiver_number": "9171985284",
}


def trigger_sos(hr, temp_c, spo2, note):
    """
    Display the SOS alert and simulate contacting emergency services.
    """

    print("\n" + "!" * 60)
    print(" CRITICAL ALERT - SOS TRIGGERED ")

    print(
        f"Time: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(
        f"Detected critical vitals -> "
        f"HR: {hr} bpm, "
        f"Temp: {temp_c}°C, "
        f"SpO2: {spo2}%"
    )

    print(f"Note: {note}")

    print("Calling emergency services (SIMULATION)...")

    print(
        f"Ambulance: "
        f"{EMERGENCY_CONTACT['ambulance_number']}"
    )

    print(
        f"Caregiver: "
        f"{EMERGENCY_CONTACT['caregiver_name']} "
        f"({EMERGENCY_CONTACT['caregiver_number']})"
    )

    print("!" * 60 + "\n")

    # Store the SOS event in the CSV file.
    log_reading(
        CSV_FILENAME,
        hr,
        temp_c,
        spo2,
        "CRITICAL",
        note + " | SOS triggered"
    )


def print_header():
    """
    Display the application header.
    """

    print("=" * 72)

    print(
        "Elder Health Monitoring & SOS Alert System"
        .center(72)
    )

    print("=" * 72)


def print_reading(
    hr,
    temp_c,
    spo2,
    status,
    note
):
    """
    Display one complete vital-sign reading.
    """

    now = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print(
        f"[{now}] "
        f"HR: {hr:3d} | "
        f"Temp: {temp_c:4.1f}°C | "
        f"SpO2: {spo2:3d}% "
        f"--> {status}"
    )

    print("   => " + note)


def user_menu():
    """
    Display the main menu.
    """

    print("\nOptions:")

    print(" [1] Normal simulation")
    print(" [2] Random simulation")
    print(" [3] Danger simulation")
    print(" [4] Edge-case simulation")
    print(" [5] Manual entry mode")
    print(" [s] Manual SOS")
    print(" [q] Quit\n")


def manual_entry_mode(check_vitals):
    """
    Take vital readings manually from the user.
    """

    print(
        "\nManual Entry Mode. "
        "Type 'back' to exit.\n"
    )

    while True:
        try:
            inp = input("Heart Rate: ").strip()

            if inp.lower() == "back":
                return

            hr = int(inp)

            temp_c = float(
                input("Temperature °C: ").strip()
            )

            spo2 = int(
                input("SpO2 %: ").strip()
            )

            status, note = check_vitals(
                hr,
                temp_c,
                spo2
            )

            print_reading(
                hr,
                temp_c,
                spo2,
                status,
                note
            )

            log_reading(
                CSV_FILENAME,
                hr,
                temp_c,
                spo2,
                status,
                "Manual entry"
            )

            if status == "Critical":

                answer = input(
                    "Trigger SOS? (y/n): "
                ).strip().lower()

                if answer == "y":
                    trigger_sos(
                        hr,
                        temp_c,
                        spo2,
                        note
                    )
                    return

        except Exception:
            print("Invalid input. Try again.")


def manual_sos():
    """
    Allow the user to manually trigger an SOS.
    """

    print("\nManual SOS Trigger")

    hr = input(
        "HR (or Enter): "
    ).strip()

    temp = input(
        "Temp (or Enter): "
    ).strip()

    spo2 = input(
        "SpO2 (or Enter): "
    ).strip()

    note = input(
        "Note: "
    ).strip()

    trigger_sos(
        int(hr) if hr else None,
        float(temp) if temp else None,
        int(spo2) if spo2 else None,
        note or "Manual SOS"
    )
