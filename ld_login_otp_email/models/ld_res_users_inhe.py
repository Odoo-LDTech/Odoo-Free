# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
import math, random


class ResUsersInhe(models.Model):
    _inherit = 'res.users'

    auth_otp = fields.Char()
    otp_timestamp = fields.Datetime()

    @staticmethod
    def generate_otp():
        string, otp = '0123456789', ''
        varlen = len(string)
        for i in range(6):
            otp += string[math.floor(random.random() * varlen)]
        return otp

    def generate_otp_in_db(self):
        otp = ResUsersInhe.generate_otp()
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.write(dict(auth_otp=otp, otp_timestamp=time_now))
        template = self.env.ref('ld_login_otp_email.mail_template_email_otp', raise_if_not_found=False)
        if template:
            template.sudo().send_mail(self.id, force_send=True)

    def verify_otp(self, otp):
        time_now = datetime.now()
        otp_time = self.otp_timestamp
        diff_time = time_now - otp_time
        diff_minutes = diff_time.total_seconds() / 60
        icp = self.env['ir.config_parameter'].sudo()
        opt_expire_duration = int(icp.get_param('ld_login_otp_email.opt_expire_duration', default=10))
        if otp == self.auth_otp and diff_minutes <= opt_expire_duration:
            return 1
        elif otp == self.auth_otp and not diff_minutes <= opt_expire_duration:
            return -1
        return 0
