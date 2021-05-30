# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dialog(models.TransientModel):
    _name = 'dialog'
    _description = 'dialog'

    
    def createNewOrderWithSaveValues(self):
        self.ensure_one()
        order = self.env['orders'].browse(self._context.get('active_ids', False))
      

        print(order.name)