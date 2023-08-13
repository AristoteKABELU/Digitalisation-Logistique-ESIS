# -*- coding: utf-8 -*-
# from odoo import http


# class Hackathon(http.Controller):
#     @http.route('/hackathon/hackathon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hackathon/hackathon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hackathon.listing', {
#             'root': '/hackathon/hackathon',
#             'objects': http.request.env['hackathon.hackathon'].search([]),
#         })

#     @http.route('/hackathon/hackathon/objects/<model("hackathon.hackathon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hackathon.object', {
#             'object': obj
#         })
