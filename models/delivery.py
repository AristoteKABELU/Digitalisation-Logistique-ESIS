from odoo import models, fields, api


class Delivery(models.Model):
    _name = 'hackathon.delivery'

    id_delivery = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('delivery.sequence'))
    delivery_date = fields.Date('delivery date')
    motif = fields.Char('motif')
    qty = fields.Integer('Qty')

    user_id = fields.Many2one(comodel_name='hackathon.user')
    stock_id = fields.Many2one(comodel_name='hackathon.stock')
