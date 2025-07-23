# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_item_degrades(self):
        items = [Item("normalItem", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        update_item = gilded_rose.items[0]
        self.assertEqual(9, update_item.sell_in)
        self.assertEqual(19, update_item.quality)

    def test_aged_brie_increases(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        update_item = gilded_rose.items[0]
        self.assertEqual(4, update_item.sell_in)
        self.assertEqual(11, update_item.quality)

    def test_backstage_pass_increases_by_3_when_5_days_left(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        update_item = gilded_rose.items[0]
        self.assertEqual(4, update_item.sell_in)
        self.assertEqual(13, update_item.quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        update_item = gilded_rose.items[0]
        self.assertEqual(80, update_item.quality)

if __name__ == '__main__':
    unittest.main()
