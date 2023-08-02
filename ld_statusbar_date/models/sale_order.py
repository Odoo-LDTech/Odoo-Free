# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state_date = fields.Datetime('State Datetime', compute='_compute_state_date', store=True)
    state_days = fields.Integer('State Days', compute='_compute_state_date', store=True)

    @api.depends('state')
    @api.onchange('date_order')
    def _compute_state_date(self):
        for rec in self:
            if not rec.state_date:
                rec.state_date = rec.date_order
            else:
                rec.state_date = fields.Datetime.now()

            rec.state_days = int((rec.state_date - rec.date_order).days) or 0
