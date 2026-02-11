# CLI Log Analyzer

A simple Python script that reads a log file and summarizes INFO, WARNING, and ERROR messages.

## Example

**Sample log (`app.log`):**
```
2025-01-10 10:15:32 INFO User login successful user_id=42
2025-01-10 10:16:01 WARNING Disk usage at 85%
2025-01-10 10:17:45 ERROR Database connection failed
2025-01-10 10:18:10 INFO File uploaded filename=report.pdf
2025-01-10 10:19:02 ERROR Timeout while contacting API
2025-01-10 10:20:15 INFO User logout user_id=42
```

**Output:**
```
Total lines: 6
INFO: 3
WARNING: 1
ERROR: 2

Errors:
 - Database connection failed
 - Timeout while contacting API
```

## Run
```
python log_analyzer.py
```
Make sure `app.log` is in the same folder.
