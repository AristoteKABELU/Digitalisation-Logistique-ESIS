from odoo import http
from odoo.http import request


class MaterielController(http.Controller):
    def _get_materiels(self):
        return request.env['hackathon.materiel'].sudo().search([])

    def _get_categories(self):
        return request.env['hackathon.category'].sudo().search([])

    def _get_registrations(self):
        return request.env['hackathon.registration'].sudo().search([])

    def _render_list_materiel(self, materiels=None):
        if materiels is None:
            materiels = self._get_materiels()
        return request.render('hackathon.listMateriel', {'materiels': materiels})

    def _render_form_materiel(self, categories=None, registrations=None):
        if categories is None:
            categories = self._get_categories()
        if registrations is None:
            registrations = self._get_registrations()
        return request.render("hackathon.formMateriel", {'categories': categories, 'registrations': registrations})

    @http.route('/materiel/list', auth='public', methods=['POST'], website=True)
    def enregistrerMateriel(self, **kw):
        return self._render_list_materiel()

    @http.route('/materiel/form/', auth='public', methods=['POST'], website=True)
    def formMateriel(self, **post):
        return self._render_form_materiel()

    @http.route('/materiel/form/create', auth='public', methods=['POST'], website=True)
    def createdMateriel(self, **post):
        request.env['hackathon.materiel'].sudo().create(post)
        return self._render_list_materiel()

    @http.route('/materiel/delete', auth='public', methods=['POST'], website=True)
    def deleteMateriel(self, **kw):
        num_serial = kw.get('num_serial_id')
        materiel = request.env['hackathon.materiel'].sudo().search([('num_serial', '=', num_serial)])
        if materiel:
            materiel.unlink()
        return self._render_list_materiel()