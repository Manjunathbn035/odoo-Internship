{
    'name': 'Kabaddi Training',
    'version': '1.0',
    'summary': 'Manage Kabaddi Training Sessions and Players',
    'description': """
        This module helps manage kabaddi training sessions and track player progress.
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'category': 'Sports',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/kabaddi_player_views.xml',
        'views/training_session_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}