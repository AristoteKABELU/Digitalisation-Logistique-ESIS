# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Consumable(models.Model):
    _name = 'hackathon.consumable'

    name = fields.Char('name')
    description = fields.Char('description')
    type = fields.Char('type')
    add_date = fields.Date('add date')
    deleted_date = fields.Date('deleted date')
    updated_date = fields.Date('updated date')

    stock_id = fields.Many2one(comodel_name='hackathon.stock')

    @api.constrains('add_date', 'deleted_date')
    def check_date(self):
        if self.add_date > self.deleted_date:
            raise ValueError('The add_date must be inferior than the delete date')
