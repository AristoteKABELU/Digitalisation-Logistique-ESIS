from odoo import models, fields, api


class Needs(models.Model):
    _name = 'hackathon.needs'

    object = fields.Text('object')
    impulsion = fields.Char('impulsion')
    description = fields.Text('description')
    reference = fields.Char('reference')
    quantity = fields.Integer('Quantity')
    Unit_price = fields.Float('Unit price')
    Total_price = fields.Float(string='Total_price', compute='calcul_price')

    user_id = fields.Many2one(comodel_name='hackathon.user')
    request_id = fields.Many2one(comodel_name='hackathon.request')
    #requests = fields.One2many(comodel_name='hackathon.request', inverse_name='need_id')

    def calcul_price(self):
        self.Total_price = self.Unit_price * self.quantity
