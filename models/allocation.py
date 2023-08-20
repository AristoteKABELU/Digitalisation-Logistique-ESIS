from odoo import models, fields, api


class Allocation(models.Model):
    _name = 'hackathon.allocation'

    motif = fields.Char('motif')
    inserted_date = fields.Date('inserted date')
    updated_date = fields.Date('updated date')
    delivery_date = fields.Date('delivery_date')
    attachment = fields.Char('attachemnt')
    given_to = fields.Char('given to')

    user_id = fields.Many2one(comodel_name='hackathon.user')

    @api.constrains('inserted_date', 'delivery_date')
    def check_date(self):
        if self.inserted_date > self.delivery_date:
            raise ValueError('The inserted date must be inferior than the delivery date')