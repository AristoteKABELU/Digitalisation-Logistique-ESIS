# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Stock(models.Model):
     _name = 'hackathon.stock'

     add_date = fields.Date('add date')
     deleted_date = fields.Date('deleted date')
     updated_date = fields.Date('updated date')
     qty = fields.Integer('quantity')
     unit = fields.Char('Unitialisation')
     
