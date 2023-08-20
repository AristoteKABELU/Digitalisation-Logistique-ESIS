# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
    _name = 'hackathon.category'

    designation = fields.Char('designation')

    materiel_ids = fields.One2many(comodel_name='hackathon.materiel', inverse_name='category_id')
