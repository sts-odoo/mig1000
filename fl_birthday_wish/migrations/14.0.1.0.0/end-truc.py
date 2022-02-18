# -*- coding: utf-8 -*-

import logging
from odoo.upgrade.util import create_column
import os

_logger = logging.getLogger(__name__)

def migrate(cr, version):


    _logger.info("ca migreeeeeuxxxx.........")
    _logger.info("ici %s", create_column)
    _logger.info("version %s", version)
    _logger.info("previous version 1 - %s", os.getenv("__base_version"))
    _logger.info("previous version 2 - %s", os.getenv("ODOO_BASE_VERSION"))
    cr.execute("UPDATE res_partner set display_name='coucou'")
