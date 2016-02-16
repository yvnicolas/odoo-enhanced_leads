# -*- coding: utf-8 -*-
{
    'name': "enhanced_leads",

    'summary': """
        Adds some features to main Odoo CRM leads""",

    'description': """
        Enables to add specific fields to lead to better manage actions on leads from a simple user interface
    """,

    'author': "Yves Nicolas",
    'website': "http://dynamease.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}