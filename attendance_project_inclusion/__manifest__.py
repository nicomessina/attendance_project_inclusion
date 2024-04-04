# -*- coding: utf-8 -*-
{
    "name": "Attendance Project Inclusion",
    "summary": """Module to add Project related data on Attendances
""",
    "description": """Module to add Project related data on Attendances
""",
    "category": "Human Resources/Attendances",
    "author": "Nicolas Messina",
    "version": "17.0.1.0.0",
    "depends": ["project", "hr_attendance", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/attendance_project_task_wizard_views.xml",
        "views/hr_attendance_views.xml",
    ],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "AGPL-3",
    "assets": {
        "web.assets_backend": [
            "attendance_project_inclusion/static/src/js/attendance_menu.js",
        ],
    },
}
