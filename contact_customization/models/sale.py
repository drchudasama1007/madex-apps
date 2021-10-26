# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, date


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_id = fields.Many2one(domain=[('sale_ok', '=', True), '|', ('expiry_date', '>', date.today()), ('expiry_date', '=', False)])
