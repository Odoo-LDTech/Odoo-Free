# -*- coding: utf-8 -*-
{
    'name': 'Status Bar Date',
    'version': '1.0',
    'summary': 'Highlights No of days the document stay in particular state.',
    'description': """Highlights No of days the document stay 
    in particular state on the statusbar widget.
    """,
    'author': 'Livedigital Technologies Private Limited',
    'company': 'Livedigital Technologies Private Limited',
    'maintainer': 'Livedigital Technologies Private Limited',
    'website': 'https://ldtech.in',
    'depends': ['web', 'sale'],
    'license': 'LGPL-3',
    'installable': True,
    'data': ['views/sale_order_view.xml'],
    'images': ['static/description/icon.jpg'],
    'assets': {
        'web.assets_backend': [
            'ld_statusbar_date/static/src/**/*',
        ],
    }
}
