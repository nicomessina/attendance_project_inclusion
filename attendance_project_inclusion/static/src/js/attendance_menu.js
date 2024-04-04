/** @odoo-module **/
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
import { useDebounced } from "@web/core/utils/timing";


patch(ActivityMenu.prototype, {
    setup(attributes) {
        super.setup(...arguments);
        this.action = useService("action");
        // Re set variable value with extended method
        this.onClickSignInOut = useDebounced(this.signInOutExtended, 200, true);

    },

    async searchReadEmployee(){
        // Call method again to include the new project related data 
        const result = await this.rpc("/hr_attendance/attendance_user_data");
        super.searchReadEmployee();
        this.employee = result;
    },

    async signInOutExtended() {
        // Extension of original method `signInOut`
        let context = {
            default_is_check_in : !this.state.checkedIn,
            default_description : this.employee.attendance_description,    
            default_project_id : this.employee.attendance_project_id,    
            default_task_id : this.employee.attendance_task_id,    
        }
        let greeting = !this.state.checkedIn ? "Welcome " : "See you later "
        navigator.geolocation.getCurrentPosition(
            async ({coords: {latitude, longitude}}) => {
                context = makeContext([context, {
                    default_latitude: latitude,
                    default_longitude: longitude,
                }])
                await this.action.doAction({
                    name: greeting+this.employee.employee_name+"!",
                    type: 'ir.actions.act_window',
                    res_model: 'attendance.project.task.wizard',
                    views: [[false, 'form']],
                    context: context,
                    target: "new"
                });
                await this.searchReadEmployee()
            },
            async err => {
                await this.action.doAction({
                    name: greeting+this.employee.employee_name+"!",
                    type: 'ir.actions.act_window',
                    res_model: 'attendance.project.task.wizard',
                    views: [[false, 'form']],
                    context: context,
                    target: "new",
                });
                await this.searchReadEmployee()
            }
        )
    }
});
