# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
    _name = 'hackathon.materiel'

    id_materiel = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('materiel.sequence'))
    num_serial = fields.Char('num_serial')

    registration_id = fields.Many2one(comodel_name='hackathon.registration')
    category_id = fields.Many2one(comodel_name='hackathon.category')
