# -*- coding: utf-8 -*-
{
    'name': "Cost Email Alert",

    'summary': """
        Send Email when any product in quotation has unit price less than its standard price. """,

    'description': """
        Send Email to the configured users during quotation generation, 
        when any product in quotation has unit price less than its standard price.
    """,

    'author': "Livedigital Technologies Private Limited",
    'website': "ldtech.in",

    'category': 'Sales',
    'version': "14.0.0.1",

    'depends': ['base', 'mail', 'sale_management'],

    'data': [
        'data/cost_mail.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'live_test_url' : 'https://www.youtube.com/watch?v=G2AaW8SBwOA'
}
