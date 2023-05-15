# -*- coding: utf-8 -*-

{
    'name': 'Payslip Excel Report',
    'version': "16.0.0.1",
    'author': "Livedigital Technologies Private Limited",
    'website': "ldtech.in",
    'category': 'Payroll',
    # "license": "LGPL-3",
    'summary': 'Excel sheet for Payslip report',
    'description': """ Payslip excel report""",
    'depends': ['base', 'hr_payroll_community'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/payslip_xls_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
