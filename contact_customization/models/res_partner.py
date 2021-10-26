# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CountryCode(models.Model):
    _name = "country.code"

    name = fields.Char("Country name")
    code = fields.Char("Country code")

    def name_get(self):
        res = []
        for country in self:
            res.append((country.id,("%s  %s") % (country.name, country.code)))
        return res


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zone = fields.Char("Zone")
    zone_number = fields.Char("Zone No.")
    street_number = fields.Char("Street No.")
    building_name = fields.Char("Building")
    building_number = fields.Char("Building No.")
    floor_number = fields.Char("Floor No.")
    number = fields.Char("Number")
    unit_number = fields.Char("Unit Number")
    floor = fields.Char('Floor')
    po_box_number = fields.Char("P.O.Box Number")
    area_code = fields.Char("Area Code")
    phone_area_code = fields.Char("Phone Area Code")
    is_sponsor = fields.Boolean("Is Sponsor")
    sponsor_id = fields.Many2one('res.partner', 'Sponsor', domain=[('is_sponsor', '=', True)])
    id_number = fields.Char("ID Number")
    id_expire_date = fields.Date("Expiry Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting For Approval'),
        ('approved', 'Approved'),
        ], string='Status', default='draft')
    country_code = fields.Many2one('country.code',string="Country code")
    person_responsible = fields.Many2one('res.partner',string="Person Responsible")
    cr_number = fields.Char("CR No.")

    #new module
    compny_id = fields.Char('Company Id')
    issue_date1 = fields.Date('Issue Date')
    expire_date1 = fields.Date('Expiry Date')
    printed_date1 = fields.Date('Print Date')
    pdf3 = fields.Binary('Scan document upload')
    trade_lic = fields.Char('Trade Licence')
    issue_date2 = fields.Date('Issue Date')
    expire_date2 = fields.Date('Expiry Date')
    printed_date2 = fields.Date('Print Date')
    pdf4 = fields.Binary('Scan document upload')
    tax_card = fields.Char('Tax Card')
    issue_date3 = fields.Date('Issue Date')
    expire_date3 = fields.Date('Expiry Date')
    printed_date3 = fields.Date('Print Date')
    pdf5 = fields.Binary('Scan document upload')

    attested_date = fields.Date('Attested Date')
    issue_date4 = fields.Date('Issue Date')
    artical_of_assoc = fields.Char('A.O.A. / Startup Doc.')
    pdf1 = fields.Binary('Scan document upload')
    comp_type = fields.Many2one('company.type', string='Company Type')
    capital = fields.Char('Capital')
    co_regis_number = fields.Char('Corporate Registration')
    issue_date5 = fields.Date('Issue Date')
    expire_date4 = fields.Date('Expiry Date')
    printed_date4 = fields.Date('Print Date')
    pdf2 = fields.Binary('Scan document upload')

    signatory_id1 = fields.Char('Signatory Id 1')
    name1 = fields.Many2one('res.partner', string="Name")
    expire_date5 = fields.Date('Expiry Date')
    pdf6 = fields.Binary('Scan document upload')
    is_sponsor1 = fields.Boolean('Is Sponsor')
    signatory_id2 = fields.Char('Signatory Id 2')
    name2 = fields.Many2one('res.partner', string="Name")
    expire_date6 = fields.Date('Expiry Date')
    pdf7 = fields.Binary('Scan document upload')
    is_sponsor2 = fields.Boolean('Is Sponsor')
    signatory_id3 = fields.Char('Signatory Id 3')
    name3 = fields.Many2one('res.partner', string="Name")
    expire_date7 = fields.Date('Expiry Date')
    pdf8 = fields.Binary('Scan document upload')
    is_sponsor3 = fields.Boolean('Is Sponsor')
    signatory_id4 = fields.Char('Signatory Id 4')
    name4 = fields.Many2one('res.partner', string="Name")
    expire_date8 = fields.Date('Expiry Date')
    pdf9 = fields.Binary('Scan document upload')
    is_sponsor4 = fields.Boolean('Is Sponsor')
    signatory_id5 = fields.Char('Signatory Id 5')
    name5 = fields.Many2one('res.partner', string="Name")
    expire_date9 = fields.Date('Expiry Date')
    pdf11 = fields.Binary('Scan document upload')
    is_sponsor5 = fields.Boolean('Is Sponsor')

    share_holder = fields.Many2one('res.partner', string='Share Holder 1')
    ID_CR_numer = fields.Char('ID/CR numer 1')
    share_percentage = fields.Char('Share percentage 1')
    shares_attachment = fields.Binary('Attachment 1')

    share_holder_2 = fields.Many2one('res.partner', string='Share Holder 2')
    ID_CR_numer_2 = fields.Char('ID/CR numer 2')
    share_percentage_2 = fields.Char('Share percentage 2')
    shares_attachment_2 = fields.Binary('Attachment 2')

    share_holder_3 = fields.Many2one('res.partner', string='Share Holder 3')
    ID_CR_numer_3 = fields.Char('ID/CR numer 3')
    share_percentage_3 = fields.Char('Share percentage 3')
    shares_attachment_3 = fields.Binary('Attachment 3')

    share_holder_4 = fields.Many2one('res.partner', string='Share Holder 4')
    ID_CR_numer_4 = fields.Char('ID/CR numer 4')
    share_percentage_4 = fields.Char('Share percentage 4')
    shares_attachment_4 = fields.Binary('Attachment 4')

    share_holder_5 = fields.Many2one('res.partner', string='Share Holder 5')
    ID_CR_numer_5 = fields.Char('ID/CR numer 5')
    share_percentage_5 = fields.Char('Share percentage 5')
    shares_attachment_5 = fields.Binary('Attachment 5')
   # attachment = fields.Char("Attachment")
   # article = fields.Char("Article of Association")
   # article_issue_date = fields.Date("Issue Date")
   # article_attested_date = fields.Date("Attested Date")
   # company_type = fields.Char("Company type")
   # capital = fields.Char("Capital")
   # cor_reg_no = fields.Char("Corporate Registration No.")
   # reg_issue_date = fields.Date("Issue Date")
   # reg_expiry_date = fields.Date("Expiry Date")
   # reg_printed_date = fields.Date("Printed Date")
   # cr_company_id = fields.Char("Company ID")
   # com_issue_date = fields.Date("Issue Date")
   # com_expiry_date = fields.Date("Expiry Date")
   # com_printed_date = fields.Date("Printed Date")
   # trade_licence = fields.Char("Trade Licence")
   # tl_issue_date = fields.Date("Issue Date")
   # tl_expiry_date = fields.Date("Expiry Date")
   # tl_printed_date = fields.Date("Printed Date")
   # tax_card = fields.Char("Tax Card")
   # tax_issue_date = fields.Date("Issue Date")
   # tax_expiry_date = fields.Date("Expiry Date")
   # tax_printed_date = fields.Date("Printed Date")
   # sig_id_1 = fields.Char("Signatory ID 1")
   # sig_name1= fields.Char('Name')
   # s1_expiry_date = fields.Date("Expiry Date")
   # sig_sponsor1 = fields.Boolean("Is Sponsor")
   # sig_id_2 = fields.Char("Signatory ID 2")
   # sig_name2 = fields.Char('Name')
   # s2_expiry_date = fields.Date("Expiry Date")
   # sig_sponsor2 = fields.Boolean("Is Sponsor")
   # sig_id_3 = fields.Char("Signatory ID 3")
   # sig_name3 = fields.Char('Name')
   # s3_expiry_date = fields.Date("Expiry Date")
   # sig_sponsor3 = fields.Boolean("Is Sponsor")
   # sig_id_4 = fields.Char("Signatory ID 4")
   # sig_name4 = fields.Char('Name')
   # s4_expiry_date = fields.Date("Expiry Date")
   # sig_sponsor4 = fields.Boolean("Is Sponsor")
   # sig_id_5 = fields.Char("Signatory ID 5")
   # sig_name5 = fields.Char('Name')
   # s5_expiry_date = fields.Date("Expiry Date")
   # sig_sponsor5 = fields.Boolean("Is Sponsor")



    def action_sned_approval_customer(self):
        for partner in self:
            partner.state = 'waiting_approval'

    def action_approve_customer(self):
        for partner in self:
            partner.state = 'approved'

    def action_draft_customer(self):
        for partner in self:
            partner.state = 'draft'

    @api.onchange('parent_id')
    def onchange_parent_id(self):
        res = super(ResPartner,self).onchange_parent_id()
        new_res = {}
        return new_res


class ComapnyType(models.Model):
	_name = 'company.type'

	name = fields.Char('')