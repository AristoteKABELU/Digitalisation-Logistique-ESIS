from odoo import http


class Login(http.Controller):
    @http.route('/loginAuthentification', auth='public', methods=['POST'], type='http',csrf=False, website=True)
    def checking(self, **kw):
        users = http.request.env['hackathon.user'].sudo().search([])
        for user in users:
            if (user.email == kw.get('email')) and (kw.get('password') == user.password) and (user.job_title == 'responsable'):
                return http.request.render('hackathon.responsablePage', {})
            elif  (user.email == kw.get('email')) and (kw.get('password') == user.password) and (user.job_title == 'subalterne'):
                return http.request.render('hackathon.subalternePage', {})
            elif  (user.email == kw.get('email')) and (kw.get('password') == user.password) and (user.job_title == 'SGDA'):
                return http.request.render('hackathon.subalternePage', {})


    @http.route('/login', auth='public', website=True)
    def loginPage(self, **kw):
        return http.request.render('hackathon.loginPage', {})