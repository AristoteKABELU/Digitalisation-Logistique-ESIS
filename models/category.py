# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
    _name = 'hackathon.category'

    id_category = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('category.sequence'))
    designation = fields.Char('designation')

    materiel_ids = fields.One2many(comodel_name='hackathon.materiel', inverse_name='category_id')
