# Elder Health Monitoring System

## Project Statement

The **Elder Health Monitoring System** is a Python-based application designed to monitor the health and vital signs of elderly individuals. The system allows health-related data to be generated or entered manually, checks the readings against predefined thresholds, provides alerts when abnormal or critical conditions are detected, and maintains a persistent record of the monitored data.

The system is designed with a modular structure to separate vital-sign processing, alert handling, and data logging.

## Project Structure

```text
src
├── vitals_module.py
├── alert_module.py
├── main.py
├── vitals_logs.csv
└── logging_module.py


```

---

## 1. Main Program — `main.py`

`main.py` is the main controller of the Elder Health Monitoring System.

### Responsibilities

- Display the main menu.
- Allow the user to select monitoring operations.
- Coordinate the different modules.
- Start vital-sign monitoring.
- Allow generated or manually entered health data.
- Check vital signs for abnormal conditions.
- Trigger appropriate alerts.
- Store monitoring results in the log file.
- Provide an option to safely exit the system.

---

## 2. Vitals Module — `vitals_module.py`

The `vitals_module.py` module manages the vital-sign data of the elderly person.

### Responsibilities

### Thresholds

Define acceptable health ranges for monitored vital signs.

Possible vital signs include:

- Heart rate
- Blood pressure
- Body temperature
- Oxygen saturation (SpO₂)

The system should compare each reading with its predefined threshold and identify whether the reading is normal, abnormal, or critical.

### Data Generation

Provide functionality to generate sample/simulated vital-sign readings.

This can be used to demonstrate and test the monitoring system without requiring physical medical sensors.

### Data Checks

Check the collected vital-sign readings against the predefined thresholds.

The module should identify:

- Normal readings
- Abnormal readings
- Critical readings requiring immediate attention

---

## 3. Alert Module — `alert_module.py`

The `alert_module.py` module manages notifications and interaction when an elderly person's health readings become abnormal or critical.

### Console Screens

Display the current health readings and their status clearly on the console.

### Example

```text
Elder Health Monitoring System
--------------------------------
Heart Rate : 82 bpm
Temperature: 36.8 °C
SpO2       : 97 %

Status: NORMAL
```

### SOS Alerts

Generate an SOS alert when a critical health condition is detected.

For example, if a vital sign crosses a critical threshold, the system should display a prominent emergency message.

```text
!!! SOS ALERT !!!

Critical health condition detected.
Immediate attention is required.
```

### Manual Entry

Allow the user or caregiver to manually enter the elderly person's vital-sign readings.

The manually entered values should be validated before being processed and logged.

---

## 4. Logging Module — `logging_module.py`

The `logging_module.py` module is responsible for maintaining a persistent record of the elderly person's health readings.

### CSV File Setup

Create and initialize the health monitoring log file when required.

The default file is:

```text
vitals_logs.csv
```

### Log Append

Add new health-monitoring records to the CSV file without deleting previous records.

Each monitoring session should be appended as a new record.

### Persistence

Ensure that health records remain stored even after the application is closed.

When the application is started again, previous monitoring records should remain available in the CSV file.

---

## 5. Health Data Logging

The system should maintain a persistent record of the elderly person's monitored health information.

A log entry may contain:

- Date
- Time
- Heart rate
- Blood pressure
- Body temperature
- SpO₂
- Data source
- Health status
- Alert status

### Example

```csv
Date,Time,Heart Rate,Blood Pressure,Temperature,SpO2,Source,Status,Alert
30-09-2026,10:30,78,120/80,36.7,98,Manual,Normal,None
30-09-2026,10:35,115,150/95,37.2,94,Generated,Abnormal,Warning
```

---

## 6. System Workflow

The general workflow of the Elder Health Monitoring System is:

1. Start the application using `main.py`.
2. Display the main menu.
3. Select the required monitoring operation.
4. Generate or manually enter the elderly person's vital-sign data.
5. Validate the entered/generated readings.
6. Compare the readings with predefined health thresholds.
7. Display the current health status.
8. Generate an alert if an abnormal or critical condition is detected.
9. Trigger an SOS alert for critical conditions.
10. Store the readings and status in `vitals_logs.csv`.
11. Return to the main menu.
12. Allow the user to safely exit the application.

---

## 7. Health Status

The system can classify readings into three general categories:

### Normal

The vital signs are within the predefined acceptable range.

```text
Status: NORMAL
```

### Abnormal

One or more readings are outside the normal range and require attention.

```text
Status: ABNORMAL
Warning: Please monitor the elderly person's condition.
```

### Critical

A reading reaches a critical threshold and requires immediate attention.

```text
Status: CRITICAL
!!! SOS ALERT !!!
Immediate medical attention may be required.
```

The threshold values should be configurable according to the requirements of the monitoring system and should not be treated as a substitute for professional medical assessment.

---

## 8. Requirements

The Elder Health Monitoring System should:

- Be implemented using Python.
- Use a modular program structure.
- Monitor important elderly health indicators.
- Support both generated and manually entered data.
- Validate user input.
- Compare readings against predefined thresholds.
- Display health status clearly.
- Provide warning and SOS alerts.
- Store monitoring data in a CSV file.
- Append new records without overwriting previous records.
- Maintain data persistence between program executions.
- Handle invalid input without unexpectedly terminating the application.
- Provide a simple console-based interface.

---

## 9. File Description

| File | Purpose |
|---|---|
| `main.py` | Main menu and program control |
| `vitals_module.py` | Vital-sign thresholds, data generation, and health-data checks |
| `alert_module.py` | Console display, SOS alerts, and manual data entry |
| `logging_module.py` | CSV setup, log appending, and data persistence |
| `vitals_logs.csv` | Persistent storage of elderly health-monitoring records |
| `statement.md` | Project statement and system requirements |

---

## 10. Objective

The primary objective of the **Elder Health Monitoring System** is to provide a simple and modular method for monitoring elderly health data, identifying potentially abnormal readings, generating appropriate alerts, and maintaining a persistent history of health observations.

The system is intended as a monitoring and educational application and does not replace professional medical diagnosis or emergency medical services.
