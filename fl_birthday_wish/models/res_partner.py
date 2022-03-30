# -*- coding: utf-8 -*-

from odoo import fields, models
import requests
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    birthday = fields.Date('Date of Birth')

    def do_stuff(self):
        url = '%s/web/login' % self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        _logger.info('PING myself at %s', url)
        requests.get(url)
