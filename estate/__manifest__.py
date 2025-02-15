{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.1",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/new_users.xml",
        "views/kanban_view.xml",
    ],
    "installable": True,
    'license': 'LGPL-3',
}
