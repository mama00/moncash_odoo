# -*- coding: utf-8 -*-
{
    'name': "Moncash",

    'summary': """
        Support of Moncash for Odoo""",

    'description': """
        this package allow you to accept payment via moncash in the odoo platforms
    """,

    'author': "Ayiti Analytics",
    'website': "https://www.ayitianalytics.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Payment Acquirers',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['payment'],

    # always loaded
    'data': [
        'views/moncash_views.xml',
        'views/payment_moncash_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'application': True,
    'post_init_hook': 'create_missing_journal_for_acquirers',
    'sequence': 345,



}
