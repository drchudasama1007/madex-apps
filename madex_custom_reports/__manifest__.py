# -*- coding: utf-8 -*-
{
    'name': 'Madex Custom Report',
    'version': '14.0.1',
    'category': 'Sale',
    'author': 'Bansi Patel',
    'summary': 'Madex Custom Report',
    'description': """
Madex Custom Report
     """,
    'depends': [
        'jt_amount_in_words','sale','purchase','account'
        # 'stock',
    ],
    'data': [
        'report/external_layout.xml',
        'report/sale_report_template.xml',
        'report/invoice_report_template.xml',
        'report/purchase_report_template.xml',
        # 'report/delivery_note_report_template.xml',
    ],
    'installable': True,
}
