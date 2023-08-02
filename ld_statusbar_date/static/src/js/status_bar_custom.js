/** @odoo-module **/

import { StatusBarField } from "@web/views/fields/statusbar/statusbar_field";
import { registry } from "@web/core/registry";

export class StatusBarFieldCustom extends StatusBarField {


    getVisibleSelection() {
        let selection = this.options;
        if (this.props.visibleSelection.length) {
            selection = selection.filter(
                (item) =>
                    this.props.visibleSelection.includes(item[0]) || item[0] === this.props.value
            );
        }

        if (this.props.record.resModel == 'sale.order'){
            return selection.map((item) => ({
                    id: item[0],
                    name: item[1],
                    isSelected: item[0] === this.props.value,
                    isFolded: false,
                    days: this.props.record.data.state_days,
                }));

        }

        return selection.map((item) => ({
                id: item[0],
                name: item[1],
                isSelected: item[0] === this.props.value,
                isFolded: false,
            }));
        }

        computeItems(){
            let res = super.computeItems();
            res.unfolded.reverse();
            return res;
        }

};

StatusBarFieldCustom.template = "ld_statusbar_date.StatusBarFieldCustom";

registry.category("fields").add("statusbar_custom", StatusBarFieldCustom);

