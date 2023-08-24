from odoo import models, fields, api


class Request(models.Model):
    _name = 'hackathon.request'

    #is_frontend_multilang = fields.Boolean(string='Is Frontend Multilang')
    id_request = fields.Integer('ID', default=lambda self: self.env['ir.sequence'].next_by_code('request.sequence'))
    object = fields.Text('object')
    applicant = fields.Char('applicant')
    imputation = fields.Char('imputation')
    state_request = fields.Integer('state request')
    dateofRequest = fields.Date('dateofRequest')

    need_ids = fields.One2many(comodel_name='hackathon.needs', inverse_name='request_id')