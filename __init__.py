# Copyright (c) 2015 Jaime van Kessel
# The BarbarianPlugin is released under the terms of the AGPLv3 or higher.

from . import BarbarianPlugin
from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("BarbarianPlugin")


def getMetaData():
    return {}


def register(app):
    return {"extension": BarbarianPlugin.BarbarianPlugin()}
