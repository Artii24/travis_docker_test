#!/usr/bin/env python3

import unittest
from script import say_hello 

class TestScript(unittest.TestCase):

  def test_hello(self):
     self.assertEqual(say_hello("Vadim"),"Hello, Vadim")

  def test_hello(self):
      self.assertEqual(say_hello("V"),"Hello, V")
  if __name__=="__main__"
  unittest.main()
