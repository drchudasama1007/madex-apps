from odoo import models, fields, api, _

class HRHolidy(models.Model):
    _inherit = 'hr.leave'

    depart_id = fields.Many2one('hr.department', string="Department")
    state = fields.Selection([
        ('draft', 'To Submit'),
        ('cancel', 'Cancelled'),  # YTI This state seems to be unused. To remove
        ('confirm', 'Draft'),
        ('refuse', 'Discarded'),
        ('validate1', 'First Approved'),
        ('validate', 'Final Approved')
    ], string='Status', compute='_compute_state', store=True, tracking=True, copy=False, readonly=False,
        help="The status is set to 'To Submit', when a time off request is created." +
             "\nThe status is 'To Approve', when time off request is confirmed by user." +
             "\nThe status is 'Refused', when time off request is refused by manager." +
             "\nThe status is 'Approved', when time off request is approved by manager.")