from odoo.addons.hr_attendance.controllers.main import HrAttendance


class HrAttendanceExtended(HrAttendance):

    @staticmethod
    def _get_employee_info_response(employee):
        response = super(
            HrAttendanceExtended, HrAttendanceExtended
        )._get_employee_info_response(employee)
        # Extend response only if the last attendance is ongoing (not check_out set)

        if employee and not employee.last_attendance_id.check_out:
            response.update(
                {
                    "attendance_description": employee.last_attendance_id.description,
                    "attendance_project_id": employee.last_attendance_id.project_id.id,
                    "attendance_task_id": employee.last_attendance_id.task_id.id,
                }
            )
        return response
