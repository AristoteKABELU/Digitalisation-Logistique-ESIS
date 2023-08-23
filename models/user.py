# -*- coding: utf-8 -*-
from odoo import models, fields, api
import bcrypt


class User(models.Model):
    _name = 'hackathon.user'

    id = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('user.sequence'))
    name = fields.Char('name')
    lastname = fields.Char('lastname')
    firstname = fields.Char('firstname')
    email = fields.Char('email')
    password = fields.Char(string='password')
    job_title = fields.Char('job_title')
    needs_ids = fields.One2many(comodel_name='hackathon.needs', inverse_name='user_id')
    registration_ids = fields.One2many(comodel_name='hackathon.registration', inverse_name='user_id')
    allocation_ids = fields.One2many(comodel_name='hackathon.allocation', inverse_name='user_id')
    delivery_ids = fields.One2many(comodel_name='hackathon.delivery', inverse_name='user_id')

    @api.model
    def create(self, values):
        if 'password' in values:
            # Chiffrer le mot de passe avant l'enregistrement
            hashed_password = bcrypt.hashpw(values['password'].encode('utf-8'), bcrypt.gensalt())
            values['password'] = hashed_password.decode('utf-8')

        return super(User, self).create(values)
