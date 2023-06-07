# -*- coding: utf-8 -*-
{
    'name': 'Email OTP based users login',
    'author': 'Livedigital Technologies Private Limited',
    'summary': 'This module lets your Odoo users enable login with email OTP.',
    'description': 'This module lets your Odoo users enable login with email OTP.',
    'version': "15.0.0.1",
    # 'price': '15.0',
    # 'currency': 'USD', 
    'license': 'LGPL-3',
    'category': 'Extra Tools','Productivity'
    "price": 1000,
    "currency": 'INR',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'data/email_otp_template.xml',
        'views/web_tmpl_enter_otp.xml',
        'views/config_settings.xml'
     ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'website': 'https://ldtech.in',
    'live_test_url' : 'https://www.youtube.com/watch?v=1EhtYYdz8Ew'
}
