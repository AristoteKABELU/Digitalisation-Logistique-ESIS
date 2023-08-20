from odoo import models, fields, api


class Needs(models.Model):
    _name = 'hackathon.needs'

    object = fields.Text('object')
    impulsion = fields.Char('impulsion')
    description = fields.Text('description')
    reference = fields.Char('reference')
    quantity = fields.Integer('Quantity')
    Unit_price = fields.Float('Unit price')
    Total_price = fields.Float('Total price')

    user_id = fields.Many2one(comodel_name='hackathon.user')
    request_id = fields.Many2one(comodel_name='hackathon.request')
