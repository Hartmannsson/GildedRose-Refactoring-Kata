# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Aged Brie":
                _update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                _update_backstage_pass(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                _update_sulfuras(item)
            elif item.name.startswith("Conjured"):
                _update_conjured(item)
            elif item.name == "Gem of Teleportation"
                _update_gem(item)
            else:
                _update_normal(item)

def clamp_quality(quality):
    return max(MIN_QUALITY, min(MAX_QUALITY, quality))

def _update_gem(item):
    item.sell_in -= 1
    degradion = 0 if item.sell_in >= 0 else -3
    item.quality = clamp_quality(item.quality - degradation)
    

def _update_normal(item):
    item.sell_in -= 1
    degradation = 2 if item.sell_in < 0 else 1
    item.quality = clamp_quality(item.quality - degradation)


def _update_aged_brie(item):
    increase = 1 if item.sell_in > 0 else 2
    item.quality = clamp_quality(item.quality + increase)
    item.sell_in -= 1

def _update_backstage_pass(item):
    item.sell_in -= 1
    if item.sell_in < 0:
        item.quality = 0
    elif item.sell_in < 5:
        item.quality = clamp_quality(item.quality + 3)
    elif item.sell_in < 10:
        item.quality = clamp_quality(item.quality + 2)
    else:
        item.quality = clamp_quality(item.quality + 1)


def _update_sulfuras(_item):
    pass

def _update_conjured(item):
    item.sell_in -= 1
    degradation = 4 if item.sell_in < 0 else 2
    item.quality = clamp_quality(item.quality - degradation)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
