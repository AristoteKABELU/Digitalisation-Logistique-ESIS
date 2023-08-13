# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
     _name = 'hackathon.materiel'

     num_serial = fields.Char('num_serial')

     registration_id = fields.Many2one(comodel_name='hackathon.registration')
     category_id = fields.Many2one(comodel_name='hackathon.category')


