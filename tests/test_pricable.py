#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-price-level
------------

Tests for `Pricable` models module.
"""
import datetime

from django.test import TestCase

from model_mommy import mommy


class TestDjango_price_level(TestCase):

    def test_get_current_price_level(self):
        price_level = mommy.make(
            "PriceLevel",
            name="Foo price level",
            takes_effect_on=datetime.date(year=2017, month=1, day=1),
        )
        result = price_level.pricable.get_current_price_level(date_time=datetime.date(year=2017, month=1, day=1))
        self.assertEqual(result, price_level)

    def test_get_current_price_level_none(self):
        price_level = mommy.make(
            "PriceLevel",
            name="Foo price level",
            takes_effect_on=datetime.date(year=2017, month=1, day=2),
        )
        result = price_level.pricable.get_current_price_level(date_time=datetime.date(year=2017, month=1, day=1))
        self.assertEqual(result, None)

    def test_get_current_price_levels(self):
        price_level = mommy.make(
            "PriceLevel",
            name="Foo price level",
            takes_effect_on=datetime.date(year=2017, month=1, day=1),
            offer_ends=datetime.date(year=2017, month=3, day=2),
        )
        price_level1 = mommy.make(
            "PriceLevel",
            name="Bar price level",
            priceable=price_level.priceable,
            takes_effect_on=datetime.date(year=2017, month=1, day=1),
            offer_ends=datetime.date(year=2017, month=2, day=2),
        )
        result = set(price_level.priceable.get_current_price_levels(date_time=datetime.date(year=2017, month=1, day=1)))
        self.assertEqual(result, set((price_level, price_level1)))

        result = set(price_level.priceable.get_current_price_levels(date_time=datetime.date(year=2017, month=2, day=5)))
        self.assertEqual(result, set((price_level,)))

