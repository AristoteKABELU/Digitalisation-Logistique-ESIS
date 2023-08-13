from odoo import models, fields, api


class Registration(models.Model):
    _name = 'hackathon.registration'

    registration_date = fields.Date('registration date')
    modification_date = fields.Date('modification date')
    deletion_date = fields.Date('deletion date')


