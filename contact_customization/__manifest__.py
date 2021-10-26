# -*- coding: utf-8 -*-
{
    'name': 'Contact Customization',
    'version': '14.0.1.0.0',
    'category': 'Sale',
    'author': 'Bansi Patel',
    'summary': 'Contact Customization',
    'description': """
Contact Customization
     """,
    'depends': [
	    'base',
        'contacts',
        'sale_management',
        'purchase',
        # 'maintenance',
        'project',
        'hr',
        'analytic',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'data/payment_term_data.xml',
        # 'data/expiry_date_notification.xml',
        # 'data/expiry_date_email_templates.xml',
        'views/res_partner_view.xml',
        'views/borrow_view.xml',
        # 'views/res_bank_view.xml',
        'views/product_view.xml',
        # 'views/maintenance_view.xml',
        # 'views/account_view.xml',
        'views/hr_employee_view.xml',
        'views/project_view.xml',
        # 'views/sale_view.xml',
        # 'views/invoice_view.xml',
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
}
