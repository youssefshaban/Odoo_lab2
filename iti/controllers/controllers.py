# -*- coding: utf-8 -*-
from odoo import http
import json
import codecs

class Iti(http.Controller):
    @http.route('/iti/iti/medicine/create', auth='public',type='json')
    def index(self,csrf=False,**kw):
            res = codecs.decode(http.request.httprequest.data, 'UTF-8')
            parsed = json.loads(res)
            result = http.request.env['medicine'].create({
                'name':parsed['name'],
                'price':parsed['price'],
                'description':parsed['description'],
                'manufacturer':parsed['manufacturer'],
            })
# 763e5bcee59a3563ae281c8306fdbbba1785fc79

    @http.route('/iti/iti/objects/', auth='public')
    def list(self, **kw):
        result = http.request.env['medicine'].search_read(
            fields=[
                'name',
                'price',
                'description',
                'manufacturer'
                ]
            )
        print(result)
        return json.dumps(result)

