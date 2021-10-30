# -*- coding: utf-8 -*-

from odoo import api, fields, models
"""
Aeroplane ticket - String
Visa costs - Number
Monthly rent - Number
Utility expenses - Number
Phone - Number
Transportation costs - Number
Working hrs per month: - Number
Rate for worker - Number
"""
class HREmployee(models.Model):
    _inherit = 'hr.employee'

    sponsor_id = fields.Many2one('res.partner', 'Sponsor', domain=[('is_sponsor', '=', True)])
    aeroplan_tikit = fields.Float("Aeroplane ticket")
    visa_cost = fields.Float("Visa costs")
    monthly_rate = fields.Float("Monthly rent")
    utility_expenses = fields.Float("Utility expenses")
    cost_phone = fields.Float("Phone")
    transportation_costs = fields.Float("Transportation costs")
    working_hour = fields.Integer("Working hrs per month",default=192)
    worker_rate = fields.Float("Rate for worker", compute='_compute_worker_rate', store=True)
    analytic_account_count = fields.Integer(compute='_analytic_account', string='Analytic Account', copy=False)

    @api.onchange('user_id')
    def onchange_user_id(self):
        if self.user_id.partner_id:
            if self.user_id.partner_id.bank_ids:
                self.write({
                    'bank_account_id' : self.user_id.partner_id.bank_ids[0]
                })

    def _analytic_account(self):
        for rec in self:
            accounts = self.env['account.analytic.account'].search([('employee_id', '=', rec.id)])
            if accounts:
                rec.analytic_account_count = len(accounts)
            else:
                rec.analytic_account_count = 0

    @api.depends('aeroplan_tikit', 'visa_cost', 'monthly_rate', 'utility_expenses', 'cost_phone', 'transportation_costs', 'working_hour')
    def _compute_worker_rate(self):
        for rec in self:
            if rec.working_hour:
                if rec.aeroplan_tikit or rec.visa_cost or rec.monthly_rate or rec.utility_expenses or rec.cost_phone or rec.transportation_costs:
                    rec.worker_rate = (rec.aeroplan_tikit+rec.visa_cost+rec.monthly_rate+rec.utility_expenses+rec.cost_phone+rec.transportation_costs)/rec.working_hour
                else:
                    rec.worker_rate = 0
            else:
                rec.worker_rate = 0

    def action_open_analytic_account(self):
        accounts = self.env['account.analytic.account'].search([('employee_id', '=', self.id)])
        action = self.env.ref('analytic.action_account_analytic_account_form').read()[0]
        if len(accounts) > 1:
            action['domain'] = [('id', 'in', accounts.ids)]
            action['context'] = {'default_employee_id': self.id}
        elif len(accounts) == 1:
            action['views'] = [(self.env.ref('analytic.view_account_analytic_account_form').id, 'form')]
            action['res_id'] = accounts.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action

class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    employee_id = fields.Many2one('hr.employee', string='Employee')