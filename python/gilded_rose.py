# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = [ItemFactory.create(item) for item in items]

    def update_quality(self):
        for item in self.items:
            print("Item before update:", item.sell_in, item.quality)
            item.update_quality()
            item.sell_in -= 1
            print("Item after update:", item.sell_in, item.quality)

    @staticmethod
    def increase_quality(item, amount=1):
        if item.quality < 50:
            item.quality += amount

    @staticmethod
    def decrease_quality(item, amount=1):
        if item.quality > 0:
            item.quality -= amount


class ItemFactory:
    @staticmethod
    def create(item):
        if item.name == "Aged Brie":
            return AgedBrie(item.sell_in, item.quality)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(item.sell_in, item.quality)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item.sell_in, item.quality)
        else:
            return NormalItem(item.name, item.sell_in, item.quality)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



class NormalItem(Item):
    def update_quality(self):
        if self.sell_in < 0:
            GildedRose.decrease_quality(self, 2)
        else:
            GildedRose.decrease_quality(self)


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)

    def update_quality(self):
        pass  # Sulfuras does not need to update quality


class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self):
        GildedRose.increase_quality(self)


class BackstagePass(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def update_quality(self):
        if self.sell_in < 1:
            self.quality = 0
        elif self.sell_in < 6:
            GildedRose.increase_quality(self, 3)
        elif self.sell_in < 11:
            GildedRose.increase_quality(self, 2)
        else:
            GildedRose.increase_quality(self)
