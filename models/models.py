# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)
import datetime
import time

class purchaseagreement(models.Model):
    _name = 'purchase.requisition'
    _inherit = ['purchase.requisition','mail.thread']


    def _cek_agreement_deadline(self):
        _logger.info('proses cek Agreemenet Deadline.....')
        sql = "select id,name,date_end from purchase_requisition where date_end = %s"
        
        date_deadline = datetime.datetime.now() 

        cr = self.env.cr
        cr.execute(sql , (date_deadline.strftime("%Y-%m-%d"),))
        res = cr.fetchall()

        
        _logger.info(date_deadline)
        purchases = self.env['purchase.requisition'].search([
                                                            ('date_end','<=',date_deadline),
                                                            ('state','!=','done')
                                                            ])
        _logger.info(purchases)


        for purchase in purchases:

            _logger.info(purchase.date_end)
            purchase.message_post(body="Purchase Agreements status otomatis Closed",
                                message_type='comment',
                                subtype='mail.mt_comment')

            purchase.state = 'done'