from odoo import models, fields, api


class Request(models.Model):
    _name = 'hackathon.request'

    object = fields.Text('object')
    applicant = fields.Char('applicant')
    imputation = fields.Char('imputation')
    state_request = fields.Integer('state request')
    dateofRequest = fields.Integer('dateofRequest')