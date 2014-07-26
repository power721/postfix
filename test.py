#!/usr/bin/env python
# -*- coding=utf8 -*-
import unittest
from convert import convert, convert_num, eval_infix, eval_postfix

class TestConvertFunctions(unittest.TestCase):
  '''
  test cases for postfix convert functions
  '''
  
  def setUp(self):
    self.scope = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}

  def test_str_var(self):
    infix = 'a + b * c + (d / e + f) * g'
    expected = 'a b c * + d e / f + g * +'
    postfix = convert(infix)
    self.assertEqual(postfix, expected)

  def test_list_var(self):
    infix = ['a', '+', 'b', '*', 'c', '+', '(', 'd', '/', 'e', '+', 'f', ')', '*', 'g']
    expected = 'a b c * + d e / f + g * +'
    postfix = convert(infix)
    self.assertEqual(postfix, expected)

  def test_tuple_var(self):
    infix = ('a', '+', 'b', '*', 'c', '+', '(', 'd', '/', 'e', '+', 'f', ')', '*', 'g')
    expected = 'a b c * + d e / f + g * +'
    postfix = convert(infix)
    self.assertEqual(postfix, expected)

  def test_str_num(self):
    infix = '12 + 5 * (9 - 8) / 3 + 5 * 3 % 4 + 0'
    expected = '12 5 9 8 - * 3 / + 5 3 * 4 % + 0 +'
    postfix = convert_num(infix)
    self.assertEqual(postfix, expected)

  def test_single(self):
    infix = '5'
    expected = '5'
    postfix = convert_num(infix)
    self.assertEqual(postfix, expected)

  def test_empty(self):
    infix = ''
    expected = ''
    postfix = convert_num(infix)
    self.assertEqual(postfix, expected)

  def test_result(self):
    infix = '12 + 5 * (9 - 8) / 3 + 5 * 3 % 4 + 0'
    postfix = convert_num(infix, rtype=list)
    self.assertEqual(eval_infix(infix), eval_postfix(postfix))

  def test_exception(self):
    pass

if __name__ == '__main__':
  unittest.main()