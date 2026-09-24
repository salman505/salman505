{
    "name": "True Tech Solutions Website",
    "version": "17.0.1.0.0",
    "summary": "Company website for True Tech Solutions (erp.truetech-sol.com)",
    "description": """
Recreates the public True Tech Solutions website (www.truetech-sol.com)
inside Odoo Website: homepage, About, Services, Solutions and Contact
pages, main menu and brand styling.
    """,
    "category": "Website",
    "author": "True Tech Solutions",
    "website": "https://www.truetech-sol.com",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/snippets.xml",
        "views/homepage.xml",
        "views/pages.xml",
        "views/layout.xml",
        "data/menus.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_truetech/static/src/scss/truetech.scss",
        ],
    },
    "installable": True,
    "application": False,
}
