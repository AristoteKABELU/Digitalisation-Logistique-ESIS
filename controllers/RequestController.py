from odoo import http


class RequestPage(http.Controller):
    # @http.route('/request/list', auth='public', methods=['POST'], website=True)
    # def listRequest(self):
    #     requests = http.request.env['hackathon.request'].sudo().search([])
    #     return http.request.render('hackathon.listRequest', {
    #         'requests': requests
    #     })

    @http.route('/request/form/', auth='public', methods=['POST'], website=True)
    def formRequest(self, **kw):
        needs = http.request.env['hackathon.needs'].sudo().search([])
        return http.request.render('hackathon.formRequest', {
            'needs': needs
        })

    @http.route('/request/form/send', auth='public', methods=['POST'], website=True)
    def sendRequest(self, **post):
        http.request.env['hackathon.request'].sudo().create({**post})
        requests = http.request.env['hackathon.request'].sudo().search([])
        return http.request.render('hackathon.listRequest', {
            'requests': requests
        })

    @http.route('/request/delete', auth='public',methods=['POST'], website=True)
    def deleteNeed(self, **kw):
        request = kw.get('object')
        object = http.request.env['hackathon.needs'].sudo().search([('object', '=', need)])
        if object:
            object.unlink()
            needs = http.request.env['hackathon.needs'].sudo().search([])
            return http.request.render('hackathon.listNeeds', {'needs': needs})


