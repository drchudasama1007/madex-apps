# -*- coding: utf-8 -*-
{
    'name': "All In One Dashboard",
    'version': '14.0.1',
    'summary': """All In One Dashboard""",
    'description': """All In One Dashboard""",
    'author': 'Bansi Patel',
    'depends': ['base','hr', 'hr_holidays','contact_customization','planning','document_management_system','account','purchase','project'],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
        'views/hr_holiday_view.xml',
    ],
    'qweb': ["static/src/xml/custom_dashboard.xml"],
    'images': ["static/description/banner.gif"],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
