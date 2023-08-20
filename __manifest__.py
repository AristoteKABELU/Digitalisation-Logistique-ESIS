# -*- coding: utf-8 -*-
{
    'name': "hackathon",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/admin/allocation_view.xml',
        'views/admin/category_view.xml',
        'views/admin/consumable_view.xml',
        'views/admin/user_views.xml',
        'views/admin/stock_views.xml',
        'views/admin/request_views.xml',
        'views/admin/registration_views.xml',
        'views/admin/needs_views.xml',
        'views/admin/materiel_views.xml',
        'views/admin/delivery_views.xml',
        'views/user_view.xml',
        'views/loginPage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}
