# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_otp_login = fields.Boolean("Enable OTP Login")
    opt_expire_duration = fields.Integer("OTP Expire Duration")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        icp = self.env['ir.config_parameter'].sudo()
        res['enable_otp_login'] = icp.get_param('ld_login_otp_mail.enable_otp_login', default=False)
        res['opt_expire_duration'] = icp.get_param('ld_login_otp_mail.opt_expire_duration', default=10)
        return res

    @api.model
    def set_values(self):
        icp = self.env['ir.config_parameter'].sudo()
        icp.set_param('ld_login_otp_mail.enable_otp_login', self.enable_otp_login)
        icp.set_param('ld_login_otp_mail.opt_expire_duration', self.opt_expire_duration)
        super(ResConfigSettings, self).set_values()