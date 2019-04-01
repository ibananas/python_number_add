# -*- coding: utf-8 -*-
# @Time     : 2019/04/01 17:00
# @Author   : 刘洪波
# @Filename : 默认.py
# @Software : PyCharm

import unittest
from python_add_number import num_add
from python_add_number import tool
from mock import Mock,patch

class TestProducer(unittest.TestCase):

    @patch.object(num_add, 'add1')
    @patch.object(num_add, 'add2')
    def test_both(self, mock_add2, mock_add1):
        self.num_add = num_add()
        mock_add1.return_value = 1
        mock_add2.return_value = 2
        self.u = tool()
        num1 = self.u.random_number(100000)
        num2 = self.u.random_number(2500000)
        self.assertEqual(self.num_add.add1(num1, num1), 1)
        self.assertEqual(self.num_add.add2(num1, num2), 2)


