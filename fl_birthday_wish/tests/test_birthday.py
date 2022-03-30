# -*- coding: utf-8 -*-
from odoo.tests import common, tagged


@tagged('coucou')
class TestStuff(common.TransactionCase):

    def test_do_test_things(self):
        self.assertTrue(True, 'il est nul ton test')
