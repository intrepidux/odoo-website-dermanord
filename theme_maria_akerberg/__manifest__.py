{
    # Theme information
    'name': "Maria Åkerberg",
    'description': """
    """,
    'category': 'Theme/Vertel',
    'version': '1.0',
    'depends': ['website', 'website_sale', 'website_imagemagick',
    ],

    # templates
    'data': [
        # ~ 'views/options.xml',
        # ~ 'views/snippets.xml',
        'views/assets.xml',
        'views/variant_template.xml',
        'views/templates.xml',
        'views/recipe.xml',
        'views/customizations.xml',
        'views/product_views.xml',
    ],

    # demo pages
    'demo': [
        # ~ 'demo/pages.xml',
    ],
    # misc settings
    'installable': True,
    'application': False,

    # Your information
    'author': "Vertel AB",
    'website': "www.vertel.se",
}
