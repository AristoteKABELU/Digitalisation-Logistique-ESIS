from odoo import http


class Hackathon(http.Controller):
    @http.route('/needs/list', auth='public', website=True, csrf=False)
    def needList(self):
        needs = http.request.env['hackathon.needs'].sudo().search([])
        return http.request.render('hackathon.listNeeds', {
            'needs': needs
        })

    @http.route('/needs/form/', auth='public', website=True, csrf=False)
    def createList(self, **post):
        return http.request.render('hackathon.formNeed', {})

    @http.route('/needs/form/create', auth='public', website=True, csrf=False)
    def needCreated(self, **post):
        http.request.env['hackathon.needs'].sudo().create({**post})
        needs = http.request.env['hackathon.needs'].sudo().search([])
        return http.request.render('hackathon.listNeeds', {
            'needs': needs
        })

    @http.route('/needs/form/edit', auth='public', website=True, csrf=False)
    def editNeed(self, **kw):
        return http.request.render('hackathon.formNeed', {})
        # need = kw.get('object_id')
        # object = http.request.env['hackathon.needs'].sudo().search([('object', '=', need)])
        # if object:
        #     object.write(kw)
        #     needs_page = http.request.env['hackathon.needs'].sudo().search([])
        #     return http.request.render('hackathon.needsPage', {
        #         'needs': needs_page
        #     })

    @http.route('/needs/delete', auth='public', website=True, csrf=False)
    def deleteNeed(self, **kw):
        need = kw.get('object_id')
        object = http.request.env['hackathon.needs'].sudo().search([('object', '=', need)])
        if object:
            object.unlink()
            needs = http.request.env['hackathon.needs'].sudo().search([])
            return http.request.render('hackathon.listNeeds', {'needs': needs})