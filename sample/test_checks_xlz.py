#!/usr/bin/env python

"""Tests for the zip storage module"""

import os
from zipfile import ZipFile

from translate.storage import directory
from translate.storage import zipw
from translate.filters import checks
from translate.lang import data

def strprep(str1, str2, message=None):
    return data.normalized_unicode(str1), data.normalized_unicode(str2), data.normalized_unicode(message)


def check_category(filterfunction):
    """Checks whether ``filterfunction`` has defined a category or not."""
    has_category = []
    classes = (checks.TeeChecker, checks.UnitChecker)

    for klass in classes:
        categories = getattr(klass, 'categories', None)
        has_category.append(categories is not None and \
                            filterfunction.__name__ in categories)
    return True in has_category


def passes(filterfunction, str1, str2):
    """returns whether the given strings pass on the given test, handling FilterFailures"""
    str1, str2, no_message = strprep(str1, str2)
    try:
        filterresult = filterfunction(str1, str2)
    except checks.FilterFailure as e:
        filterresult = False
    filterresult = filterresult and check_category(filterfunction)
    return filterresult


def fails(filterfunction, str1, str2, message=None):
    """returns whether the given strings fail on the given test, handling only FilterFailures"""
    str1, str2, message = strprep(str1, str2, message)
    try:
        filterresult = filterfunction(str1, str2)
    except checks.SeriousFilterFailure as e:
        filterresult = True
    except checks.FilterFailure as e:
        if message:
            exc_message = e.messages[0]
            filterresult = exc_message != message
            print(exc_message.encode('utf-8'))
        else:
            filterresult = False
    filterresult = filterresult and check_category(filterfunction)
    return not filterresult


def fails_serious(filterfunction, str1, str2, message=None):
    """returns whether the given strings fail on the given test, handling only SeriousFilterFailures"""
    str1, str2, message = strprep(str1, str2, message)
    try:
        filterresult = filterfunction(str1, str2)
    except checks.SeriousFilterFailure as e:
        if message:
            exc_message = e.messages[0]
            filterresult = exc_message != message
            print(exc_message.encode('utf-8'))
        else:
            filterresult = False
    filterresult = filterresult and check_category(filterfunction)
    return not filterresult


def check_xlz_units():
    """Tests basic functionality."""
    d = zipw.ZIPFile("Oringinal_ES_TW.xlz.xlz")
    stdchecker = checks.StandardChecker(checks.CheckerConfig(targetlanguage='zh_ui'))
    for unit in d.getunits():
        if fails(stdchecker.endpunc, unit.source, unit.target):
            print(unit.source, unit.target)


if __name__=='__main__':
    check_xlz_units()
