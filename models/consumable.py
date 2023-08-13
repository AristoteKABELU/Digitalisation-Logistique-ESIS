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