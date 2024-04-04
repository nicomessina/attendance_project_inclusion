from odoo import fields, models
from odoo.addons.hr_attendance.controllers.main import HrAttendance


class AttendanceProjectTaskWizard(models.TransientModel):
    _name = "attendance.project.task.wizard"
    _description = "Attendance Project Task Wizard"

    project_id = fields.Many2one(comodel_name="project.project")
    task_id = fields.Many2one(
        comodel_name="project.task",
        domain="[('project_id','=', project_id), ('project_id','!=',False)]",
    )
    description = fields.Text()
    employee_id = fields.Many2one(
        comodel_name="hr.employee", default=lambda self: self.env.user.employee_id
    )
    attendance_id = fields.Many2one(
        comodel_name="hr.attendance", related="employee_id.last_attendance_id"
    )
    latitude = fields.Float()
    longitude = fields.Float()
    is_check_in = fields.Boolean()

    def action_process_check_in_out(self):
        # Call method that handles the check in/out of employee
        HrAttendance.systray_attendance(HrAttendance, self.latitude, self.longitude)
        self.attendance_id.write(
            {
                "project_id": self.project_id.id,
                "task_id": self.task_id.id,
                "description": self.description,
            }
        )
        # Trigger reload to refresh the checkInOut widget data
        return {"type": "ir.actions.client", "tag": "reload"}
