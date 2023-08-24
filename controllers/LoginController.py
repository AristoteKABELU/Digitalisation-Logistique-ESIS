from odoo import http
import bcrypt


class LoginController(http.Controller):
    ROLE_PAGES = {
        'responsable': 'hackathon.responsablePage',
        'subalterne': 'hackathon.subalternePage',
        'SGDA': 'hackathon.SGDAPage',
    }

    def _check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    @http.route('/loginAuthentification', auth='public', methods=['POST'], type='http', csrf=False, website=True)
    def checking(self, **kw):
        email = kw.get('email')
        password = kw.get('password')

        users = http.request.env['hackathon.user'].sudo().search([])

        for user in users:
            if user.email == email and self._check_password(password, user.password):
                page = self.ROLE_PAGES.get(user.job_title)
                if page:
                    return http.request.render(page, {})

    @http.route('/', auth='public', website=True)
    def loginPage(self):
        return http.request.render('hackathon.loginPage', {})
