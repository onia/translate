# -*- coding: utf-8 -*-
#
# Copyright 2008 Zuza Software Foundation
#
# This file is part of The Translate Toolkit.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""Test the various functions for combining and extracting accesskeys and
labels"""

from translate.convert import accesskey


def test_get_label_and_accesskey():
    """test that we can extract the label and accesskey components from an
    accesskey+label string"""
    assert accesskey.extract("") == ("", "")
    assert accesskey.extract("File") == ("File", "")
    assert accesskey.extract("&File") == ("File", "F")
    assert accesskey.extract("~File", "~") == ("File", "F")
    assert accesskey.extract("_File", "_") == ("File", "F")


def test_ignore_entities():
    """test that we don't get confused with entities and a & access key
    marker"""
    assert accesskey.extract("Set &browserName; as &Default") != ("Set &browserName; as &Default", "b")
    assert accesskey.extract("Set &browserName; as &Default") == ("Set &browserName; as Default", "D")


def test_alternate_accesskey_marker():
    """check that we can identify the accesskey if the marker is different"""
    assert accesskey.extract("~File", "~") == ("File", "F")
    assert accesskey.extract("&File", "~") == ("&File", "")


def test_unicode():
    """test that we can do the same with unicode strings"""
    assert accesskey.extract("Eḓiṱ") == ("Eḓiṱ", "")
    assert accesskey.extract("E&ḓiṱ") == ("Eḓiṱ", "ḓ")
    assert accesskey.extract("E_ḓiṱ", "_") == ("Eḓiṱ", "ḓ")
    label, akey = accesskey.extract("E&ḓiṱ")
    assert label, akey == ("Eḓiṱ", "ḓ")
    assert isinstance(label, str) and isinstance(akey, str)


def test_empty_string():
    """test that we can handle and empty label+accesskey string"""
    assert accesskey.extract("") == ("", "")
    assert accesskey.extract("", "~") == ("", "")


def test_end_of_string():
    """test that we can handle an accesskey at the end of the string"""
    assert accesskey.extract("Hlola&") == ("Hlola&", "")


def test_combine_label_accesskey():
    """test that we can combine accesskey and label to create a label+accesskey
    string"""
    assert accesskey.combine("File", "F") == "&File"
    assert accesskey.combine("File", "F", "~") == "~File"


def test_uncombinable():
    """test our behaviour when we cannot combine label and accesskey"""
    assert accesskey.combine("File", "D") is None
    assert accesskey.combine("File", "") is None
    assert accesskey.combine("", "") is None
