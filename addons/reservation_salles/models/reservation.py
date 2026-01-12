from odoo import models, fields

class ReservationSalle(models.Model):
    _name = 'reservation.salle'
    _description = 'Réservation de Salle'

    name = fields.Char(string="Nom de la salle", required=True)
    date_reservation = fields.Date(
        string="Date de réservation",
        required=True
    )
    heure_debut = fields.Float(
        string="Heure de début"
    )
    heure_fin = fields.Float(
        string="Heure de fin"
    )
    responsable_id = fields.Many2one(
        'res.users',
        string="Responsable",
        default=lambda self: self.env.user
    )
    state = fields.Selection(
        [
            ('brouillon', 'Brouillon'),
            ('confirmee', 'Confirmée'),
            ('annulee', 'Annulée')
        ],
        string="Statut",
        default='brouillon'
    )
