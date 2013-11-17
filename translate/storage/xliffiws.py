#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 Zuza Software Foundation
#
# This file is part of the Translate Toolkit.
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

"""Module for handling XLIFF files for translation.

The official recommendation is to use the extention .xlf for XLIFF files.
"""
# This file is for Idiom xliff file, a type of xliff file.
#
from lxml import etree

from translate.misc.multistring import multistring
from translate.storage import base, lisa, xliff
from translate.storage.lisa import getXMLspace
from translate.storage.placeables.lisa import xml_to_strelem, strelem_to_xml
from translate.storage.workflow import StateEnum as state
from translate.misc.xml_helpers import namespaced

# TODO: handle translation types

ID_SEPARATOR = "\04"
# ID_SEPARATOR is commonly used through toolkit to generate compound
# unit ids (for instance to concatenate msgctxt and msgid in po), but
# \04 is an illegal char in XML 1.0, ID_SEPARATOR_SAFE will be used
# instead when converting between xliff and other toolkit supported
# formats
ID_SEPARATOR_SAFE = "__%04__"


class xliffunitiws(xliff.xliffunit):
    """A single term in the xliff file."""

    rootNode = "trans-unit"
    languageNode = "source"
    textNode = ""
    namespace = 'urn:oasis:names:tc:xliff:document:1.2'
    namespaceiws = 'http://www.idiominc.com/ws/asset'

    _default_xml_space = "default"

    #TODO: id and all the trans-unit level stuff

    S_UNTRANSLATED = state.EMPTY
    S_NEEDS_TRANSLATION = state.NEEDS_WORK
    S_NEEDS_REVIEW = state.NEEDS_REVIEW
    S_TRANSLATED = state.UNREVIEWED
    S_SIGNED_OFF = state.FINAL

    statemap = {
                "new": S_UNTRANSLATED + 1,
                "needs-translation": S_NEEDS_TRANSLATION,
                "needs-adaptation": S_NEEDS_TRANSLATION + 1,
                "needs-l10n": S_NEEDS_TRANSLATION + 2,
                "needs-review-translation": S_NEEDS_REVIEW,
                "needs-review-adaptation": S_NEEDS_REVIEW + 1,
                "needs-review-l10n": S_NEEDS_REVIEW + 2,
                "translated": S_TRANSLATED,
                "signed-off": S_SIGNED_OFF,
                "final": S_SIGNED_OFF + 1,
                }

    statemap_r = dict((i[1], i[0]) for i in statemap.items())

    STATE = {
        S_UNTRANSLATED: (state.EMPTY, state.NEEDS_WORK),
        S_NEEDS_TRANSLATION: (state.NEEDS_WORK, state.NEEDS_REVIEW),
        S_NEEDS_REVIEW: (state.NEEDS_REVIEW, state.UNREVIEWED),
        S_TRANSLATED: (state.UNREVIEWED, state.FINAL),
        S_SIGNED_OFF: (state.FINAL, state.MAX),
    }

    # metadata & status
    metadata={}
    markupdata={}

    def __init__(self, source, empty=False, **kwargs):
        """Override the constructor to set xml:space="preserve"."""
        super(xliffunitiws, self).__init__(source, empty, **kwargs)
        if empty:
            return
        lisa.setXMLspace(self.xmlelement, "preserve")

    def namespacediws(self, name):
        """Returns name in Clark notation.

        For example ``namespaced("source")`` in an XLIFF document
        might return::

            {urn:oasis:names:tc:xliff:document:1.1}source

        This is needed throughout lxml.
        """
        return namespaced(self.namespaceiws, name)

    def getunitid(self):
        #"""get unit id."""
        unitid = self.xmlelement.get('id')
        return unitid
    ''' Suggestion: the following two overide functions only for display or export data with tags,
    #    Or special checking related to tags
    def getText(self, languageNode, xml_space):
        #"""get Text with internal tag."""
        # Here used a very simple way
        #TODO: add xml_space support when needed
        content = ''
        if languageNode.text!=None:
            content += languageNode.text
        for child in languageNode:
            #if child.tag==xmlns_default+'ph':# Idiom seems only have the ph tag.
            content += str(child.get('x'))# Here can control wether export the tag content
            if child.tail!=None:
                content += child.tail
        return content
    
    def getNodeText(self, languageNode, xml_space="preserve"):
        """Retrieves the term from the given :attr:`languageNode`."""
        if languageNode is None:
            return None
        if self.textNode:
            terms = languageNode.iterdescendants(self.namespaced(self.textNode))
            if terms is None:
                return None
            try:
                return self.getText(next(terms), xml_space)
            except StopIteration:
                # didn't have the structure we expected
                return None
        else:
            return self.getText(languageNode, xml_space)
    '''
    def getmetadataNode(self):
        #"""get metadata nodes."""
        metadataNode = None
        metadataNode = self.xmlelement.find(self.namespacediws("segment-metadata"))
        return metadataNode

    def getmetadata(self):
        #"""get metadata nodes."""
        self.metadata = {}
        metadataNode = self.getmetadataNode()
        statusNode = metadataNode.find(self.namespacediws("status"))
        self.metadata['max_segment_length'] = metadataNode.get('max_segment_length')
        self.metadata['ws_word_count'] = metadataNode.get('ws_word_count')
        self.metadata['tm_score'] = metadataNode.get('tm_score')
        self.metadata['tm_origin'] = statusNode.get('tm_origin')
        self.metadata['translation_status'] = statusNode.get('translation_status')
        self.metadata['match-quality'] = statusNode.get('match-quality')
        return self.metadata

    def getmarkupdata(self):
        #"""get metadata nodes."""
        self.markupdata = {}
        markupNode = None
        markupNode = self.xmlelement.findall(self.namespacediws("markup-seg"))
        for item in markupNode:
            sequence = item.get("sequence")
            self.markupdata[sequence] = item.text#.encode('utf-8')
        return self.markupdata

    def setmetadata(self, translation_status=None):
        #"""get metadata nodes."""
        metadataNode = self.getmetadataNode()
        statusNode = metadataNode.find(self.namespacediws("status"))
        if translation_status: statusNode.set('translation_status', translation_status)

class xlifffileiws(xliff.xlifffile):
    """Class representing a XLIFF file store."""
    UnitClass = xliffunitiws
    Name = _("XLIFF Translation File")
    Mimetypes = ["application/x-xliff", "application/x-xliff+xml"]
    Extensions = ["xlf", "xliff", "sdlxliff"]
    rootNode = "xliff"
    bodyNode = "body"
    XMLskeleton = '''<?xml version="1.0" ?>
<xliff version='1.1' xmlns='urn:oasis:names:tc:xliff:document:1.1'>
<file original='NoName' source-language='en' datatype='plaintext'>
<body>
</body>
</file>
</xliff>'''
    namespace = 'urn:oasis:names:tc:xliff:document:1.1'
    unversioned_namespace = 'urn:oasis:names:tc:xliff:document:'

    suggestions_in_format = True
    """xliff units have alttrans tags which can be used to store suggestions"""

    def __init__(self, *args, **kwargs):
        self._filename = None
        lisa.LISAfile.__init__(self, *args, **kwargs)
        self._messagenum = 0
    def __str__(self):
        return etree.tostring(self.document, pretty_print=False,
                              xml_declaration=True, encoding='utf-8').decode('utf-8')
