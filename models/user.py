# -*- coding: utf-8 -*-

from odoo import models, fields, api


class User(models.Model):
     _name = 'hackathon.user'

     name = fields.Char('name')
     lastname = fields.Char('lastname')
     firstname = fields.Char('firstname')
     email = fields.Char('email')
     password = fields.Char('password')
     job_title = fields.Char('job_title')

     needs_ids = fields.One2many(comodel_name='hackathon.needs', inverse_name='user_id')
     registration_ids = fields.One2many(comodel_name='hackathon.registration', inverse_name='user_id')
     allocation_ids = fields.One2many(comodel_name='hackathon.allocation', inverse_name='user_id')
     delivery_ids = fields.One2many(comodel_name='hackathon.delivery', inverse_name='user_id')
