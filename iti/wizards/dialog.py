# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dialog(models.TransientModel):
    _name = 'dialog'
    _description = 'dialog'

    
    def createNewOrderWithSaveValues(self):
        self.ensure_one()
        order = self.env['orders'].browse(self._context.get('active_ids', False))
        print (order.order_lines)
        # new_instance = self.env['orders'].create([order])
        customer = self.env['res.partner'].browse(order.name.id)
        print (customer.id)
        newOrder = self.env['orders'].create({
            'date': order.date,
            'name':customer.id,
            'total':order.total
            })
        for  lines in order.order_lines :
            medicine = self.env['medicine'].browse(lines.name.id)
            order = self.env['orders'].browse(newOrder.id)
            self.env['order_lines'].create(
            {
                'name':medicine.id,
                'qty':lines.qty,
                'sub_total':lines.sub_total,
                'orderItem': order.id
            }
        )
        # print(new_instance)