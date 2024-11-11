{
    "name": "Trip Log",
    "version": "17.0.0.0",
    "autor": "walt-sergio",
    "description": """
        Trip Log module to log trip informations
    """,
    "category": "",

    "data": [
        # SECURITY
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        # VIEWS
        'views/trip_views.xml',
        'views/route_views.xml',
        'views/route_type_views.xml',
        'views/emplacement_views.xml',
        # MENU
        'views/trip_menus.xml',
        # DATAS Files
        # Default data for route_type
        # "data/route.type.csv",
    ],

    "depends": ["base", "fleet", "hr", "account", "mail"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
