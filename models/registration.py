from odoo import models, fields, api


class Registration(models.Model):
    _name = 'hackathon.registration'

    id_registration = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('registration.sequence'))
    registration_date = fields.Date('registration date')
    modification_date = fields.Date('modification date')
    deletion_date = fields.Date('deletion date')

    user_id = fields.Many2one(comodel_name='hackathon.user')
    materiel_ids = fields.One2many(comodel_name='hackathon.materiel', inverse_name='registration_id')

    @api.constrains('registration_date', 'modification_date', 'deletion_date')
    def check_date(self):
        if self.registration_date > self.modification_date:
            raise ValueError('The registration date must be inferior than the modification date')
        elif self.registration_date > self.deletion_date:
            raise ValueError('The registration date must be inferior than the delete date')
        elif self.modification_date > self.deletion_date:
            raise ValueError('The modification must be inferior than the delete date')
