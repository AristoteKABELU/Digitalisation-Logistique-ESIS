from odoo import http


class RequestPage(http.Controller):
    @http.route('/request', auth='public', website=True)
    def Needlist(self, **kw):
        needs= http.request.env['hackathon.needs'].sudo().search([])
        print(needs)
        return http.request.render('hackathon.requestPage', {
            'needs': needs
        })

    class ResqueSend(http.Controller):

        @http.route('/send_request', methods=['POST'], csrf=True, auth='public', website=True)
        def Needlist(self, **post):
            requests = http.request.env['hackathon.request'].sudo().create(**post)


