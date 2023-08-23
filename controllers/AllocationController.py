from odoo import http
from odoo.http import request


class AllocationControle(http.Controller):
    def _get_allocations(self):
        return request.env['hackathon.allocation'].sudo().search([])

    def _render_list_allocations(self):
        allocations = self._get_allocations()
        return request.render("hackathon.listAllocation", {'allocations': allocations})

    def _get_users(self):
        return request.env['hackathon.user'].sudo().search([])

    def _render_form_allocation(self, users=None):
        if users is None:
            users = self._get_users()
        return request.render('hackathon.formAllocation', {'users': users})

    @http.route('/allocation/list', auth='public', methods=['POST'], website=True)
    def list_allocation(self, **post):
        return self._render_list_allocations()

    @http.route('/allocation/form/', auth='public', methods=['POST'], website=True)
    def form_allocation(self):
        return self._render_form_allocation()

    @http.route('/allocation/form/create', auth='public', methods=['POST'], website=True)
    def create_allocation(self, **post):
        request.env['hackathon.allocation'].sudo().create(post)
        return self._render_list_allocations()

    @http.route('/allocation/form/edit', auth='public', methods=['POST'], website=True, csrf=False)
    def edit_allocation(self, **kw):
        request.env['hackathon.needs'].sudo().write(kw)

    @http.route('/allocation/delete', auth='public', methods=['POST'], website=True, csrf=False)
    def delete_allocation(self, **kw):
        allocation = kw.get('motif_id')
        motif = request.env['hackathon.allocation'].sudo().search([('motif', '=', allocation)])
        if motif:
            motif.unlink()
        return self._render_list_allocations()