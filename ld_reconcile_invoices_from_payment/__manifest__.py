# -*- coding: utf-8 -*-
{
    'name': 'Multi Invoice Payment For Customer and Vendor',
    'version': '14.0',
    'category': 'Sales',
    'summary': 'User can do payment of multiple invoice at same time of same customer.',

    'depends': ['sale_management', 'account', ],

    'data': [
        'security/ir.model.access.csv',
        'views/account_payment.xml',
        'wizard/multi_invoice.xml',
        "license": "LGPL-3",

    ],

    'author': "Livedigital Technologies Private Limited",
    'website': "ldtech.in",
    'support': 'suresh.hiyal@ldtech.in',
    'maintainer': 'Livedigital Technologies Private Limited',
    'images': ['static/description/img/icon.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
