from odoo import models, fields, api


class Delivery(models.Model):
    _name = 'hackathon.delivery'

    delivery_date = fields.Date('delivery date')
    motif = fields.Char('motif')
    qty = fields.Integer('Qty')

    user_id = fields.Many2one(comodel_name='hackathon.user')
    stock_id = fields.Many2one(comodel_name='')
