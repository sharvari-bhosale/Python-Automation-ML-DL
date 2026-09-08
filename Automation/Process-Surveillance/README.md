
# Process Surveillance

## Description

Process Surveillance is a Python-based system monitoring and automation project that collects information about running processes and system resources.

The project scans running processes, monitors CPU and RAM usage, records process information into log files, executes the monitoring task periodically, and sends the generated log file through email.

## Features

* Fetch information about running processes
* Display Process ID (PID)
* Display process name
* Display process username
* Display process status
* Monitor CPU usage of processes
* Monitor RAM usage of processes
* Identify processes based on CPU usage
* Identify processes based on RAM usage
* Record process creation time
* Generate system monitoring log files
* Perform automatic periodic execution
* Send generated log files through email
* Handle inaccessible or terminated processes safely
* Provide command-line help and usage information

## Technologies Used

* Python
* psutil
* schedule
* smtplib
* EmailMessage
* OS module
* DateTime module

## Python Modules

```text
psutil
schedule
```

The project also uses Python's built-in modules such as `sys`, `os`, `time`, `datetime`, and `smtplib`.

## Project Structure

```text
Process-Surveillance/
│
├── ProcessSurveillance.py
├── README.md
├── requirements.txt
│
├── screenshots/
│   ├── 01_Command_Execution.png
│   ├── 02_Command_Execution.png
│   ├── 03_System_Report.png
│   ├── 04_Process_Information.png
│   └── 05_Email.png
│
└── logs/
    └── .gitkeep
```

## Functions

### `ProcessScan()`

Scans all currently running processes and collects information such as PID, process name, username, status, CPU usage, RAM usage, and process creation time.

### `Top10CpuProcess()`

Retrieves process information and sorts the processes according to CPU usage in descending order.

### `Top10RamProcess()`

Retrieves process information and sorts the processes according to RAM usage in descending order.

### `send_mail()`

Sends the generated log file as an email attachment using Gmail's SMTP server.

### `PlatformSurvillance()`

Creates the specified folder if required, generates a timestamped log file, stores the collected system information, and performs the monitoring operation.

### `main()`

Handles command-line arguments, displays help and usage information, and starts the periodic scheduler.

## How to Run

### 1. Install Python

Make sure Python is installed on your system.

Check the Python version:

```bash
python --version
```

### 2. Install Required Modules

Open Command Prompt inside the project folder and run:

```bash
pip install psutil schedule
```

### 3. Run the Program

The program accepts two command-line arguments:

```text
python ProcessSurveillance.py Time_Interval Folder_Name
```

Example:

```bash
python ProcessSurveillance.py 1 Logs
```

Here:

* `1` = Execute the monitoring task every 1 minute
* `Logs` = Folder where the log files will be generated

### 4. Display Help

```bash
python ProcessSurveillance.py --h
```

or

```bash
python ProcessSurveillance.py --H
```

### 5. Display Usage

```bash
python ProcessSurveillance.py --u
```

or

```bash
python ProcessSurveillance.py --U
```

## Log File

The project automatically creates log files containing the collected process and system information.

The log file name is generated using the current date and time, allowing multiple monitoring records to be maintained separately.

## Email Notification

The project can send the generated log file through email as an attachment.

The email functionality uses:

```text
SMTP_SSL
smtp.gmail.com
Port 465
```

For security, email credentials should not be stored directly in the source code when uploading the project to GitHub.

## Sample Command

```bash
python ProcessSurveillance.py 1 Logs
```

Sample execution:

```text
--------------------------------------------------
--- Platform Surveillance Started ---
--------------------------------------------------

Scheduler started successfully
Press Ctrl + C to abort the automation script
```

## Advantages

* Automates system monitoring
* Provides process-level information
* Helps monitor CPU and RAM usage
* Maintains monitoring records through log files
* Supports periodic execution
* Provides email-based log notification
* Uses Python system-monitoring libraries

## Future Enhancements

* Add a graphical user interface
* Add real-time CPU and RAM graphs
* Add process search by name
* Add process search by PID
* Add process status statistics
* Add battery monitoring
* Add disk usage monitoring
* Add network usage monitoring
* Store monitoring data in a database
* Add configurable email settings

## Conclusion

Process Surveillance demonstrates the use of Python for system monitoring, process management, file handling, scheduling, logging, and email automation. It provides an automated way to collect process information and maintain monitoring records.
