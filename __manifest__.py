# -*- coding: utf-8 -*-
{
    'name': "hackathon",

    'icon': "/home/snoop/dev-odoo/my_addons/hackathon/static/src/img/logoEsis.png",

    'summary': """ 
        Dans le souci de la digitalisation Esis, à travers son centre de recherche et développement CREDIA organise un Hackathon basé sur "ESIS-Digital", un projet conduit par Credia sur l'informatisation et la numérisation pour améliorer les processus internes de ESIS.
        Dans cette première édition du Hackathon Esis Digital, il est demandé aux participants de proposer une solution qui répond aux différents besoins de la logistique à ESIS.
        """,

    'description': """
        Gestion de la logistique
    """,

    'author': "Groupe Mugiwara",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

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
        'views/needs.xml',
        'views/request.xml',
        'views/responsable.xml',
        'views/subalterne.xml',
        'views/login.xml',
        'views/responsable.xml',
        'views/allocation.xml',
        'views/materiel.xml',
        'views/admin/delivery_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}
