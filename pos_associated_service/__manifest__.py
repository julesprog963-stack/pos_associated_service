{
    "name": "POS Associated Service",
    "summary": "Associated service workflow for POS products",
    "description": "Adds associated service fields on products and a POS popup to add service lines alongside main products.",
    "version": "17.0.1.0.0",
    "category": "Point of Sale",
    "author": "JDA SOLUTIONS",
    "price": 1.00,
    "currency": "USD",
    "license": "LGPL-3",
    "depends": ["product", "point_of_sale"],
    "data": [
        "views/product_template_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_associated_service/static/src/js/pos_associated_service.js",
            "pos_associated_service/static/src/xml/pos_associated_service_templates.xml",
        ],
    },
    "images": [
        "static/description/screenshot_01.png",
        "static/description/screenshot_02.png",
        "static/description/screenshot_03.png",
        "static/description/screenshot_04.png",
        "static/description/screenshot_05.png",
        "static/description/screenshot_06.png",
    ],
    "installable": True,
    "application": False,
}
