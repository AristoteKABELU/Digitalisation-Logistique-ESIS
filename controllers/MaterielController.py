# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Materiel(http.Controller):
    @http.route('/materiel/list', auth='public', methods=['POST'], website=True)
    def enregistrerMateriel(self, **kw):
        materiels = http.request.env['hackathon.materiel'].sudo().search([])
        return http.request.render('hackathon.listMateriel', {
            'materiels': materiels
        })


    @http.route('/materiel/form/', auth='public', methods=['POST'], website=True)
    def createMateriel(self, **post):
        categories = http.request.env['hackathon.category'].sudo().search([])
        registrations = http.request.env['hackathon.registration'].sudo().search([])
        return request.render("hackathon.formMateriel", {'categories': categories, 'registrations': registrations})



    @http.route('/materiel/form/create', auth='public', methods=['POST'],  website=True)
    def createdMateriel(self, **post):
        http.request.env['hackathon.materiel'].sudo().create({**post})
        materiels = http.request.env['hackathon.materiel'].sudo().search([])
        return http.request.render('hackathon.listMateriel', {
            'materiels': materiels
        })

    @http.route('/materiel/delete', auth='public', methods=['POST'], website=True)
    def deleteMteriel(self, **kw):
        materiel = kw.get('num_serial_id')
        motif = http.request.env['hackathon.materiel'].sudo().search([('num_serial', '=', materiel)])
        print(motif)
        if motif:
            motif.unlink()
            materiels = http.request.env['hackathon.materiel'].sudo().search([])
            return http.request.render('hackathon.listMateriel', {
                'materiels': materiels
            })