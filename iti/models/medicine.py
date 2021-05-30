# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medicine(models.Model):
    _name = 'medicine'
    _description = 'medicine'

    name = fields.Char()
    price = fields.Float()
    description = fields.Text()
    manufacturer = fields.Char()