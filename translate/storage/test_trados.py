# -*- coding: utf-8 -*-

from pytest import mark, importorskip
importorskip("BeautifulSoup")

from translate.storage import test_base
from translate.storage import trados


def test_unescape():
    # NBSP
    assert trados.unescape(r"Ordre du jour\~:") == "Ordre du jour\u00a0:"
    assert trados.unescape(r"Association for Road Safety \endash  Conference") == "Association for Road Safety –  Conference"


def test_escape():
    # NBSP
    assert trados.escape("Ordre du jour\u00a0:") == r"Ordre du jour\~:"
    assert trados.escape("Association for Road Safety –  Conference") == r"Association for Road Safety \endash  Conference"

#@mark.xfail(reason="Lots to implement")
#class TestTradosTxtTmUnit(test_base.TestTranslationUnit):
#    UnitClass = trados.TradosUnit
#
#@mark.xfail(reason="Lots to implement")
#class TestTrodosTxtTmFile(test_base.TestTranslationStore):
#    StoreClass = trados.TradosTxtTmFile
