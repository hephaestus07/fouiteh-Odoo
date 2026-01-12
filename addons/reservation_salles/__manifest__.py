{
    'name': 'Réservation de Salles',
    'version': '1.0',
    'summary': 'Gestion et réservation des salles',
    'description': """
Module de réservation de salles.
Permet de réserver des salles selon une date, une heure
et un responsable.
""",
    'category': 'Administration',
    'author': 'Aamir',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/reservation_views.xml',
    ],
    'installable': True,
    'application': True,
}
