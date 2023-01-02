# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers import main
from odoo.http import request
from odoo.exceptions import AccessDenied


class LdWebHome(main.Home):

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        if request.httprequest.method == 'POST':
            icp = request.env['ir.config_parameter'].sudo()
            enable_otp_login = icp.get_param('ld_login_otp_email.enable_otp_login')
            if not enable_otp_login:
                return super().web_login(redirect)
            try:
                uid = request.env['res.users'].search([('login', '=', request.params['login'])])
                if uid:
                    login, passwd = request.params['login'], request.params['password']
                    vals = dict(uid=uid.id, db=request.session.db, login=login, passwd=passwd)
                    uid.sudo().generate_otp_in_db()
                    return request.render("ld_login_otp_email.verify_otp_template", vals)

                request.params['login_success'] = True
                return request.redirect(self._login_redirect(uid, redirect=redirect))
            except AccessDenied as e:
                pass
        return super().web_login(redirect)

    @http.route('/web/verify/otp', type='http', auth="none", csrf=False)
    def web_verify_otp(self, **kw):
        entered_otp, uid = request.params.get('otp'), request.params.get('uid')
        res = request.env['res.users'].browse(int(uid)).sudo().verify_otp(entered_otp)
        login, passwd = request.params['login'], request.params['passwd']
        vals = dict(uid=uid, db=request.session.db, login=login, passwd=passwd,
                    wrong_login=False, otp_expire=False)
        if res == 1:
            try:
                uid = request.session.authenticate(request.session.db,
                                                   request.params['login'],
                                                   request.params['passwd'])
            except AccessDenied as e:
                vals.update(wrong_login=True)
                return request.render("ld_login_otp_email.verify_otp_template", vals)

            redirect = request.params['redirect']
            return request.redirect(self._login_redirect(uid, redirect=redirect))

        elif res == -1:
            vals.update(otp_expire=True)
            return request.render("ld_login_otp_email.verify_otp_template", vals)

        vals.update(wrong_otp=True)
        return request.render("ld_login_otp_email.verify_otp_template", vals)

