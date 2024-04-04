# Attendance Project Inclusion

Module to add Project related data on Attendances

**Table of Contents**

- Features
- Configuration
- Usage
- Dependencies
- Limitations, Issues & Bugs

---

## Features

- Create TransientModel **attendance.project.task.wizard** to add Project, Task and Description on User's current Attendance.

- Add `project_id`, `task_id` and `description` on **hr.attendance**
    On Form view:
    - Description is required if there is no check out set
    - Project and Task are required if a new record is being created. Not applicable on existing records

- Extend CheckInOut widget:
    - Open wizard to add Project, Task and Description on Check In.
    - Open wizard to extend current Description on Check Out.
    - All the fields on the wizard are required.

---

## Configuration

- No prior configuration needed.

---

## Usage

- On either the CheckInOut widget or the Attendances app the project, task and description fields would be present.

---

## Dependencies

### Odoo modules dependencies

| Module          | Why used?                                                | Side effects |
| --------------- | -------------------------------------------------------- | ------------ |
| hr              |  To use the Employee model                               |              |
| project         |  To use the Project and Task models                      |              |
| hr_attendance   |  To extend CheckInOut widget and Attendance model        |              |

### Python library dependencies

The module doesn't require any external Python libraries.

---

## Limitations, Issues & Bugs

No limitations, issues or bugs reported to date.

---
