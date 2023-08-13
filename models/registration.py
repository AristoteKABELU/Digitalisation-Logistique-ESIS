from odoo import models, fields, api


class Registration(models.Model):
    _name = 'hackathon.registration'

    registration_date = fields.Date('registration date')
    modification_date = fields.Date('modification date')
    deletion_date = fields.Date('deletion date')

    user_id = fields.Many2one(comodel_name='hackathon.user')
    materiel_ids = fields.One2many(comodel_name='hackathon.materiel', inverse_name='registration_id')

