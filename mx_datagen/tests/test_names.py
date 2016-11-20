# -*- coding: utf-8 -*-
"""Tests for name module"""

import unittest

from mx_datagen.constants import ROOT
from mx_datagen.new_names import Name

class Names(unittest.TestCase):
    """Tests for Name module"""
    def setUp(self):
        with open(ROOT + '/data_source/info_names.json', 'r') as jfile:
            self.data = json.load(jfile)

    def test_01_get_name(self):
        """Gets a name and check parameters given"""
        self.assertIn(Name().firstname(), self.data)
