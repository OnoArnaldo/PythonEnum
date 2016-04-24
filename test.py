# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from enum import Enum


class NoYes(Enum):
    NO = 'no'
    YES = 'yes'

    _zero_value = 'no'


class NoYesMaybe(Enum):
    NO = 'no'
    YES = 'yes'
    MAYBE = 'maybe'


class Choices(Enum):
    EMPTY = ''
    OPTION_ONE = 'option 1'
    OPTION_TWO = 'option 2'


class SortOrder(Enum):
    NONE = 0
    ASC = 1
    DESC = 2


class TestEnum(unittest.TestCase):
    def testVariable(self):
        no = NoYes.NO
        self.assertEqual(no, NoYes.NO)
        self.assertNotEqual(no, NoYes.YES)

        yes = NoYes.from_value('yes')
        self.assertEqual(yes, NoYes.YES)
        self.assertNotEqual(yes, NoYes.NO)

    def testZeroValue(self):
        self.assertFalse(NoYes.NO)
        self.assertTrue(NoYes.YES)

    def testCompareDifferentClass(self):
        self.assertNotEqual(NoYes.NO, NoYesMaybe.NO)
        self.assertNotEqual(NoYes.YES, NoYesMaybe.YES)


class TestEnumWithEmpty(unittest.TestCase):
    def test(self):
        self.assertTrue(Choices.OPTION_ONE)
        self.assertTrue(Choices.OPTION_TWO)

        self.assertFalse(Choices.EMPTY)


class TestEnumWithZero(unittest.TestCase):
    def test(self):
        self.assertTrue(SortOrder.ASC)
        self.assertTrue(SortOrder.DESC)

        self.assertFalse(SortOrder.NONE)