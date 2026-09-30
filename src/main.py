# main.py

import time

from vitals_module import (
    simulate_vitals,
    check_vitals
)

from logging_module import (
    ensure_csv_header,
    log_reading,
    CSV_FILENAME
)

from alert_module import (
    trigger_sos,
    print_header,
    print_reading,
    user_menu,
    manual_entry_mode,
    manual_sos
)


# Time between automatic readings.
SAMPLE_INTERVAL = 2.0


def run_simulation(mode="normal"):
    """
    Run automatic vital-sign simulation.
    """

    print(
        f"\n[INFO] Simulation started ({mode}). "
        "Press Ctrl+C to stop."
    )

    try:

        while True:

            # Generate readings.
            hr, temp_c, spo2 = simulate_vitals(mode)

            # Check readings.
            status, note = check_vitals(
                hr,
                temp_c,
                spo2
            )

            # Display readings.
            print_reading(
                hr,
                temp_c,
                spo2,
                status,
                note
            )

            # Save readings.
            log_reading(
                CSV_FILENAME,
                hr,
                temp_c,
                spo2,
                status,
                note
            )

            # Trigger SOS if critical.
            if status == "Critical":

                trigger_sos(
                    hr,
                    temp_c,
                    spo2,
                    note
                )

                print(
                    "[INFO] Returning to menu..."
                )

                time.sleep(2)

                return

            # Wait before next reading.
            time.sleep(SAMPLE_INTERVAL)

    except KeyboardInterrupt:

        print(
            "\n[INFO] Simulation stopped."
        )


def main():
    """
    Main controller for the application.
    """

    # Make sure CSV file is ready.
    ensure_csv_header(CSV_FILENAME)

    # Display application header.
    print_header()

    while True:

        # Display menu.
        user_menu()

        choice = input(
            "Select: "
        ).strip().lower()

        if choice == "1":

            run_simulation("normal")

        elif choice == "2":

            run_simulation("random")

        elif choice == "3":

            run_simulation("danger")

        elif choice == "4":

            run_simulation("edge")

        elif choice == "5":

            manual_entry_mode(
                check_vitals
            )

        elif choice == "s":

            manual_sos()

        elif choice == "q":

            print(
                "Exiting... Stay safe!"
            )

            break

        else:

            print(
                "Invalid option."
            )


if __name__ == "__main__":
    main()
