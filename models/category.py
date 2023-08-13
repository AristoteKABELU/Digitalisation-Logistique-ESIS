# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
     _name = 'hackathon.category'

     designation = fields.Char('designation')
