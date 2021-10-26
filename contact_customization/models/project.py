# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, date


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def send_task_deadline_notification(self):
        tasks = self.search([('date_deadline', '=', date.today())])
        template = self.env.ref('ehcs_customization.task_deadline_mail_template')
        for task in tasks:
            template.send_mail(task.id)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.model
    def send_project_deadline_notification(self):
        projects = self.search([('date', '=', date.today())])
        template = self.env.ref('ehcs_customization.project_deadline_mail_template')
        for project in projects:
            template.send_mail(project.id)
