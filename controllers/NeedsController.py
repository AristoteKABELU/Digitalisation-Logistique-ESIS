from odoo import http


class Hackathon(http.Controller):
    @http.route('/needs', auth='public', website=True)
    def Needlist(self, **kw):
        needs = http.request.env['hackathon.needs'].sudo().search([])
        return http.request.render('hackathon.needsPage', {
            'needs': needs
        })

    @http.route('/delete_need', auth='public',methods=['POST'], website=True, csrf=False)
    def DeleteNeed(self, **post):
        need = post.get('object_id')
        print(len(post))
        object = http.request.env['hackathon.needs'].sudo().browse(need)
        print(object)
        if object:
            return "Done"
            #object.unlink()



