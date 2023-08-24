from odoo import http


class RequestController(http.Controller):
    MODEL_NAME = 'hackathon.request'
    TEMPLATE_LIST = 'hackathon.listRequest'
    TEMPLATE_FORM = 'hackathon.formRequest'

    def _get_requests(self):
        return http.request.env[self.MODEL_NAME].sudo().search([])

    def _get_needs(self):
        return http.request.env['hackathon.needs'].sudo().search([])

    def _render_list_requests(self, requests=None):
        if requests is None:
            requests = self._get_requests()
        print(requests)
        return http.request.render(self.TEMPLATE_LIST, {'requests': requests})

    def _render_form_request(self, needs=None):
        if needs is None:
            needs = self._get_needs()
        return http.request.render(self.TEMPLATE_FORM, {'needs': needs})

    @http.route('/request/list', auth='public', methods=['POST'], website=True)
    def listRequest(self):
        return self._render_list_requests()

    @http.route('/request/form/', auth='public', methods=['POST'], website=True)
    def formRequest(self, **kw):
        return self._render_form_request()

    @http.route('/request/form/send', auth='public', methods=['POST'], website=True)
    def sendRequest(self, **post):
        http.request.env[self.MODEL_NAME].sudo().create(post)
        return self._render_list_requests()

    @http.route('/request/delete', auth='public', methods=['POST'], website=True)
    def deleteRequest(self, **kw):
        object_id = kw.get('object')
        obj = http.request.env[self.MODEL_NAME].sudo().search([('object', '=', object_id)])
        if obj:
            obj.unlink()
        return self._render_list_requests()