from odoo import models, fields, api


class Allocation(models.Model):
    _name = 'hackathon.allocation'

    motif = fields.Char('motif')
    inserted_date = fields.Date('inserted date')
    updated_date = fields.Date('updated date')
    delivery_date = fields.Date('delivery_date')
    attachment = fields.Char('attachemnt')
    given_to = fields.Char('given to')




