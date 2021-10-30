# -*- coding: utf-8 -*-
from odoo import http

class Antonio(http.Controller):
    @http.route('/inicio', auth='public')
    # def inicio(self, **kw):
    #     return "Hola mundo, bienvenidos a la web de Antonio (inicio)"

    @http.route('/', auth='public')
    def index(self, **kw):
        return http.request.render('antonio.inicio')

    @http.route('/inicio', auth='public')
    def inicio(self, **kw):
        return http.request.render('antonio.inicio')

    @http.route('/contacto', auth='public')
    def Contacto(self, **kw):
        return http.request.render('antonio.contacto')

# class Antonio(http.Controller):
#     @http.route('/antonio/antonio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/antonio/antonio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('antonio.listing', {
#             'root': '/antonio/antonio',
#             'objects': http.request.env['antonio.antonio'].search([]),
#         })

#     @http.route('/antonio/antonio/objects/<model("antonio.antonio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('antonio.object', {
#             'object': obj
#         })
