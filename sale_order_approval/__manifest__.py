# -*- coding: utf-8 -*-
{
    'name': "Sale Order Approval",
    'summary': """
        Sale Order Approval
        """,
    'description': """
    Sale Order Approval
    =========================
        Sale Order Approval- Only users with particular group access will be able to approve the order.
    """,
    'author': "Bansi Patel",
    'category': 'sale',
    'version': '14.0.0.1.0',
    'depends': [
        'sale'
    ],
    'data': [
        'security/security.xml',
        'views/sale_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
