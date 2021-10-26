# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, date
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warranty_start_date = fields.Date('Warranty Start Date')
    warranty_end_date = fields.Date('Warranty End Date')
    #expiry_date = fields.Date("Expity Date")
    product_brand_name = fields.Many2one('product.brand', string='Product Brand Name')
    delivery_terms = fields.Char("Delivery Terms")
    expiry_date = fields.Char("Expiry", compute='difference_date', store=True)

    @api.depends('warranty_start_date', 'warranty_end_date')
    def difference_date(self):
        for rec in self:
            fmt = '%Y-%m-%d'
            if rec.warranty_start_date and rec.warranty_end_date:
                start_date = rec.warranty_start_date
                end_date = rec.warranty_end_date
                d1 = datetime.strptime(str(start_date), fmt)
                d2 = datetime.strptime(str(end_date), fmt)
                if d2 > d1:
                    # rec.expiry_date = (d2 - d1).days
                    # r = relativedelta.relativedelta(d2, d1).years * 12
                    r = d2.month - d1.month + 12 * (d2.year - d1.year)
                    # print(f'{r} months')
                    if r == 0:
                        d = (d2 - d1).days
                        rec.expiry_date = f"{d} days"
                    if 28 > r > 0:
                        print(r)
                        rec.expiry_date = f'{r} months'
                    if r > 12:
                        y = r/12
                        rec.expiry_date = f'{float("{:.2f}".format(y))} years'
                else:
                    raise UserError('End date should be superior than start day')

    @api.model
    def send_product_deadline_notification(self):
        products = self.search([('expiry_date', '=', date.today())])
        if products:
            mail_body = """
                    <b>Please take the follow up of following Products. Listed Products are expired today</b><br/><br/>\
                    <table style='border: 1px solid black'>\
                    <tr>\
                        <td style='border: 1px solid black; padding:5px'><b>Product Name</b></td>\
                    </tr>\
            """
            for product in products:
                mail_body += """
                    <tr>\
                        <td style='border: 1px solid black; padding:5px'>"""+product.name+"""</td>\
                    </tr>\
                """
            mail_body += """</table>"""
            template = self.env.ref("ehcs_customization.product_deadline_mail_template")
            template.body_html = mail_body
            template.email_to = product[0].company_id.email
            template.send_mail(product[0].id)


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Brands for products'

    name = fields.Char('Brand')
