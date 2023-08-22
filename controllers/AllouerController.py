from odoo import http
from odoo.http import request


class Allouer(http.Controller):
    @http.route('/allocation/list', auth='public', methods=['POST'], website=True)
    def listAllocation(self, **post):
        allocations = http.request.env['hackathon.allocation'].sudo().search([])
        return request.render("hackathon.listAllocation", {'allocations': allocations})

    @http.route('/allocation/form/', auth='public', methods=['POST'], website=True)
    def formAllocation(self):
        users = http.request.env['hackathon.user'].sudo().search([])
        return http.request.render('hackathon.formAllocation', {'users': users})

    @http.route('/allocation/form/create', auth='public', methods=['POST'], website=True)
    def createAllocation(self, **post):
        http.request.env['hackathon.allocation'].sudo().create({**post})
        allocations = http.request.env['hackathon.allocation'].sudo().search([])
        return request.render("hackathon.listAllocation", {'allocations': allocations})
        # self.needList(self, post)

    @http.route('/allocation/form/edit', auth='public', methods=['POST'], website=True, csrf=False)
    def editAllocation(self, **kw):
        http.request.env['hackathon.needs'].sudo().write(kw)

    @http.route('/allocation/delete', auth='public', methods=['POST'], website=True, csrf=False)
    def deleteAllocation(self, **kw):
        allocation = kw.get('motif_id')
        motif = http.request.env['hackathon.allocation'].sudo().search([('motif', '=', allocation)])
        print(motif)
        if motif:
            motif.unlink()
            allocation_page = http.request.env['hackathon.allocation'].sudo().search([])
            return http.request.render('hackathon.listAllocation', {
                'allocation': allocation_page
            })