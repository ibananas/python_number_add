# -*- coding: utf-8 -*-
# @Time     : 2018/09/01 00:00
# @Author   : 刘洪波
# @Filename : 默认.py
# @Software : PyCharm

import unittest
from python_add_number import num_add
from mock import Mock,patch

class TestProducer(unittest.TestCase):

    @patch.object(num_add, 'add1')
    @patch.object(num_add, 'add2')
    def test_both(self, mock_add2, mock_add1):
        self.num_add = num_add()
        mock_add1.return_value = 1
        mock_add2.return_value = 2
        num1 = "2649821731631836529481632803462831616487712734074314936141303241873417434716340124362304724324324324324323412121323164329751831"
        num2 = "1045091731748365195814509145981509438583247509149821493213241431431319999999999999999999999999999999999999999999999999341344779"
        self.assertEqual(self.num_add.add1(num1, num1), 1)
        self.assertEqual(self.num_add.add2(num1, num2), 2)


