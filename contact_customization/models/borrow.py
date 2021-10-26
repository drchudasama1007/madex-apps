# -*- coding: utf-8 -*-
from odoo import api, fields, models

class BorrowType(models.Model):
    _name = 'borrow.type'

    name = fields.Char("Name")


class BorrowBorrow(models.Model):
    _name = 'borrow.borrow'

    name = fields.Char("Name")
    financing_id = fields.Many2one('res.partner', 'Financing Partner')
    responsive_id = fields.Many2one('res.partner', 'Responsible')
    borrow_type_id = fields.Many2one('borrow.type', 'Type')
    contact = fields.Char("Contact Number")
    commencement_date = fields.Date("Commencement Date")
    duration = fields.Integer("Duration (months)")
    calculation_type = fields.Selection([('interest','By Interest'),('monthly','By monthly payment'),('flexible','Flexible Amount')], string="Calculation Type")
    interest = fields.Integer("Interest Rate")
    monthly_payment = fields.Integer("Monthly Payment")

    date_first_payment = fields.Date("Date of First Payment")
    date_end_contract = fields.Date("Date of End of Contract")
    due_days = fields.Integer("Due Days")
    equipment_cost = fields.Float("Equipment Cost")
    advance_payment = fields.Float("Advance Payment")

    financing_equipment_account_id = fields.Many2one('account.account', 'Financing Equipment Account')
    financing_interest_account_id = fields.Many2one('account.account', 'Financing Interest Account')

    purchase_ids = fields.Many2many('purchase.order', string='Material Requisition', compute='_purchase_load')

    def _purchase_load(self):
        for rec in self:
            purchase_orders = self.env['purchase.order'].search([('borrow_id', '=', rec.id)])
            if purchase_orders:
                rec.purchase_ids = [(6, 0, purchase_orders.ids)]
            else:
                rec.purchase_ids = False

    def create_purchase_order(self):
        return {'name': 'Purchase Order',
                'view_type': 'form',
                'views': [(self.env.ref('purchase.purchase_order_form').id, 'form')],
                'res_model': 'purchase.order',
                'view_id': self.env.ref('purchase.purchase_order_form').id,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'context': {'default_borrow_id': self.id}
                }


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    borrow_id = fields.Many2one(comodel_name="borrow.borrow", string="Borrow")
    no_quantity = fields.Integer(compute='compute_from_line', string='Qauntity')

    @api.depends('order_line')
    def compute_from_line(self):
        for rec in self:
            if rec.order_line:
                qty = 0
                for line in rec.order_line:
                    qty = qty + line.product_qty
                rec.no_quantity = qty
            else:
                rec.no_quantity = 0
