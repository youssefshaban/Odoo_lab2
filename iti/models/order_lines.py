# -*- coding: utf-8 -*-

from odoo import models, fields, api


class order_lines(models.Model):
    _name = 'order_lines'
    _description = 'order_lines'

    name = fields.Many2one("medicine")
    qty = fields.Float()
    sub_total = fields.Float(compute='_compute')
    orderItem = fields.Many2one("orders")


    @api.onchange('qty')
    def _compute(self):
        for line in self:
            line.sub_total = (line.name.price * line.qty)

