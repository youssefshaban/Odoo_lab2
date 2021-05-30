# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orders(models.Model):
    _name = 'orders'
    # _inherit = 'res.partner'
    _description = 'orders'
    

    name = fields.Many2one('res.partner')
    # channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner', 'partner_id', 'channel_id', copy="false")
    # meeting_ids = fields.Many2many('mail.meeting', 'mail_channel_profile_partner', 'partner_id', 'meeting_id', copy="false")
    order_lines = fields.One2many("order_lines","orderItem")
    total = fields.Float(compute='_compute')
    date = fields.Date()
    
    @api.onchange('order_lines')
    def _compute(self):
        for line in self:
            t = 0
            for i in line.order_lines:
                t = t+i.sub_total
            line.total = t