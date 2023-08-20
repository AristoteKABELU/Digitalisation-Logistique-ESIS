from odoo import http


class Login(http.Controller):
    @http.route('/loginAuthentification', auth='public', website=True)
    def checking(self, **kw):
        for user in http.request.env['hackathon.user'].sudo().search([]):
            if user.job_title == 'responsable' and kw.get('password') == user.password:
                print(user.name)
            elif user.job_title == 'subalterne' and kw.get('password') == user.password:
                print(user.name)
            elif user.job_title == 'SGDA' and kw.get('password') == user.password:
                print(user.name)
            # else:
            #     return {'warning': {'title': 'warning',
            #                         'message': 'mail or password invalid'}}

            # return http.request.render('hackathon.listing', {
            #     'root': '/hackathon/hackathon',
            # })

    @http.route('/login', auth='public', website=True)
    def loginPage(self, **kw):
        return http.request.render('hackathon.loginPage', {})