from odoo import http


class NeedsController(http.Controller):
    MODEL_NAME = 'hackathon.needs'
    TEMPLATE_LIST = 'hackathon.listNeeds'
    TEMPLATE_FORM = 'hackathon.formNeed'

    def _get_needs(self):
        return http.request.env[self.MODEL_NAME].sudo().search([])

    def _render_list_needs(self, needs=None):
        if needs is None:
            needs = self._get_needs()
        return http.request.render(self.TEMPLATE_LIST, {'needs': needs})

    def _render_form_need(self):
        return http.request.render(self.TEMPLATE_FORM, {})

    @http.route('/needs/list', auth='public', website=True, methods=['POST'])
    def needList(self):
        return self._render_list_needs()

    @http.route('/needs/form/', auth='public', website=True, methods=['POST'])
    def createList(self, **post):
        return self._render_form_need()

    @http.route('/needs/form/create', auth='public', website=True, methods=['POST'])
    def needCreated(self, **post):
        http.request.env[self.MODEL_NAME].sudo().create(post)
        return self._render_list_needs()

    @http.route('/needs/form/edit', auth='public', website=True, methods=['POST'])
    def editNeed(self, **kw):
        return self._render_form_need()

    @http.route('/needs/delete', auth='public', website=True, methods=['POST'])
    def deleteNeed(self, **kw):
        object_id = kw.get('object_id')
        object = http.request.env[self.MODEL_NAME].sudo().search([('object', '=', object_id)])
        if object:
            object.unlink()
        return self._render_list_needs()