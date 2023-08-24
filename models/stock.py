# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Stock(models.Model):
    _name = 'hackathon.stock'

    id_stock = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('stock.sequence'))
    add_date = fields.Date('add date')
    deleted_date = fields.Date('deleted date')
    updated_date = fields.Date('updated date')
    qty = fields.Integer('quantity')
    unit = fields.Char('Unitialisation')

    delivery_ids = fields.One2many(comodel_name='hackathon.delivery', inverse_name='stock_id')
    consomable_ids = fields.One2many(comodel_name='hackathon.consumable', inverse_name='stock_id')

    @api.constrains('add_date', 'deleted_date')
    def check_date(self):
        if self.add_date > self.deleted_date:
            raise ValueError('The add_date must be inferior than the delete date')
