# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
     _name = 'hackathon.materiel'

     num_serial = fields.Char('num_serial')

