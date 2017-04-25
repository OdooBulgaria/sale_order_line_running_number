# -*- coding: utf-8 -*-
from openerp import models, fields, api


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    @api.one
    def _get_running_number(self):
        '''Assigns a running number to the SO line, starting from 1 onwards '''
        so_lines = self.search(args=[('order_id', '=', self.order_id.id)])

        i = 1
        for so_line in so_lines:
            if so_line.id == self.id:
                self.running_number = i
                break
            i += 1

    running_number = fields.Integer('Running Number', compute=_get_running_number)
