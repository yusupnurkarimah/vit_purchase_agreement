# -*- coding: utf-8 -*-
from odoo import http

# class VitPurchaseAgreement(http.Controller):
#     @http.route('/vit_purchase_agreement/vit_purchase_agreement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_purchase_agreement/vit_purchase_agreement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_purchase_agreement.listing', {
#             'root': '/vit_purchase_agreement/vit_purchase_agreement',
#             'objects': http.request.env['vit_purchase_agreement.vit_purchase_agreement'].search([]),
#         })

#     @http.route('/vit_purchase_agreement/vit_purchase_agreement/objects/<model("vit_purchase_agreement.vit_purchase_agreement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_purchase_agreement.object', {
#             'object': obj
#         })