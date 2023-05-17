# -*- coding: utf-8 -*-
from odoo import fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    def action_preview_delivery_slip(self):
        return {
            'target': 'new',
            'type': 'ir.actions.act_url',
            'url': '/report/pdf/stock.report_deliveryslip/%s' % self.id
        }