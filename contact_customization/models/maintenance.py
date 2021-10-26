# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    equipment_brand = fields.Char('Brand')
    tool_equipment_assign_to = fields.Char('Tool/Equipment Assign To')
