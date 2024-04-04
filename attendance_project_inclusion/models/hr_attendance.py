from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    project_id = fields.Many2one(comodel_name="project.project")
    task_id = fields.Many2one(
        comodel_name="project.task",
        domain="[('project_id','=', project_id), ('project_id','!=',False)]",
    )
    description = fields.Text()
