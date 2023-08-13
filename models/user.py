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
