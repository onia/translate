#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 Zuza Software Foundation
#
# This file is part of translate.
#
# translate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""This module stores information and functionality that relates to plurals."""


languages = {
'af': ('Afrikaans', 2, '(n != 1)'),
'ak': ('Akan', 2, 'n > 1'),
'am': ('Amharic', 2, 'n > 1'),
'an': ('Aragonese', 2, '(n != 1)'),
'ar': ('Arabic', 6,
       'n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5'),
'arn': ('Mapudungun; Mapuche', 2, 'n > 1'),
'ast': ('Asturian; Bable; Leonese; Asturleonese', 2, '(n != 1)'),
'az': ('Azerbaijani', 2, '(n != 1)'),
'be': ('Belarusian', 3,
       'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2'),
'bg': ('Bulgarian', 2, '(n != 1)'),
'bn': ('Bengali', 2, '(n != 1)'),
'bn_IN': ('Bengali (India)', 2, '(n != 1)'),
'bo': ('Tibetan', 1, '0'),
'br': ('Breton', 2, 'n > 1'),
'bs': ('Bosnian', 3,
       'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2'),
'ca': ('Catalan; Valencian', 2, '(n != 1)'),
'ca@valencia': ('Catalan; Valencian (Valencia)', 2, '(n != 1)'),
'cs': ('Czech', 3, '(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2'),
'csb': ('Kashubian', 3,
        'n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2'),
'cy': ('Welsh', 2, '(n==2) ? 1 : 0'),
'da': ('Danish', 2, '(n != 1)'),
'de': ('German', 2, '(n != 1)'),
'dz': ('Dzongkha', 1, '0'),
'el': ('Greek, Modern (1453-)', 2, '(n != 1)'),
'en': ('English', 2, '(n != 1)'),
'en_GB': ('English (United Kingdom)', 2, '(n != 1)'),
'en_ZA': ('English (South Africa)', 2, '(n != 1)'),
'eo': ('Esperanto', 2, '(n != 1)'),
'es': ('Spanish; Castilian', 2, '(n != 1)'),
'et': ('Estonian', 2, '(n != 1)'),
'eu': ('Basque', 2, '(n != 1)'),
'fa': ('Persian', 1, '0'),
'ff': ('Fulah', 2, '(n != 1)'),
'fi': ('Finnish', 2, '(n != 1)'),
'fil': ('Filipino; Pilipino', 2, '(n > 1)'),
'fo': ('Faroese', 2, '(n != 1)'),
'fr': ('French', 2, '(n > 1)'),
'fur': ('Friulian', 2, '(n != 1)'),
'fy': ('Frisian', 2, '(n != 1)'),
'ga': ('Irish', 5, 'n==1 ? 0 : n==2 ? 1 : n<7 ? 2 : n<11 ? 3 : 4'),
'gd': ('Gaelic; Scottish Gaelic', 4, '(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3'),
'gl': ('Galician', 2, '(n != 1)'),
'gu': ('Gujarati', 2, '(n != 1)'),
'gun': ('Gun', 2, '(n > 1)'),
'ha': ('Hausa', 2, '(n != 1)'),
'he': ('Hebrew', 2, '(n != 1)'),
'hi': ('Hindi', 2, '(n != 1)'),
'hy': ('Armenian', 1, '0'),
'hr': ('Croatian', 3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
'ht': ('Haitian; Haitian Creole', 2, '(n != 1)'),
'hu': ('Hungarian', 2, '(n != 1)'),
'ia': ("Interlingua (International Auxiliary Language Association)", 2, '(n != 1)'),
'id': ('Indonesian', 1, '0'),
'is': ('Icelandic', 2, '(n != 1)'),
'it': ('Italian', 2, '(n != 1)'),
'ja': ('Japanese', 1, '0'),
'jv': ('Javanese', 2, '(n != 1)'),
'ka': ('Georgian', 1, '0'),
'kk': ('Kazakh', 1, '0'),
'km': ('Central Khmer', 1, '0'),
'kn': ('Kannada', 2, '(n != 1)'),
'ko': ('Korean', 1, '0'),
'ku': ('Kurdish', 2, '(n != 1)'),
'kw': ('Cornish', 4, '(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3'),
'ky': ('Kirghiz; Kyrgyz', 1, '0'),
'lb': ('Luxembourgish; Letzeburgesch', 2, '(n != 1)'),
'ln': ('Lingala', 2, '(n > 1)'),
'lo': ('Lao', 1, '0'),
'lt': ('Lithuanian', 3, '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)'),
'lv': ('Latvian', 3, '(n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2)'),
'mai': ('Maithili', 2, '(n != 1)'),
'mfe': ('Morisyen', 2, '(n > 1)'),
'mg': ('Malagasy', 2, '(n > 1)'),
'mi': ('Maori', 2, '(n > 1)'),
'mk': ('Macedonian', 2, 'n==1 || n%10==1 ? 0 : 1'),
'ml': ('Malayalam', 2, '(n != 1)'),
'mn': ('Mongolian', 2, '(n != 1)'),
'mr': ('Marathi', 2, '(n != 1)'),
'ms': ('Malay', 1, '0'),
'mt': ('Maltese', 4,
       '(n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : (n%100>10 && n%100<20 ) ? 2 : 3)'),
'nah': ('Nahuatl languages', 2, '(n != 1)'),
'nap': ('Neapolitan', 2, '(n != 1)'),
'nb': ('Bokmål, Norwegian; Norwegian Bokmål', 2, '(n != 1)'),
'ne': ('Nepali', 2, '(n != 1)'),
'nl': ('Dutch; Flemish', 2, '(n != 1)'),
'nn': ('Norwegian Nynorsk; Nynorsk, Norwegian', 2, '(n != 1)'),
'nqo': ("N'Ko", 2, '(n > 1)'),
'nso': ('Pedi; Sepedi; Northern Sotho', 2, '(n != 1)'),
'oc': ('Occitan (post 1500)', 2, '(n > 1)'),
'or': ('Oriya', 2, '(n != 1)'),
'pa': ('Panjabi; Punjabi', 2, '(n != 1)'),
'pap': ('Papiamento', 2, '(n != 1)'),
'pl': ('Polish', 3,
       '(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
'pms': ('Piemontese', 2, '(n != 1)'),
'ps': ('Pushto; Pashto', 2, '(n != 1)'),
'pt': ('Portuguese', 2, '(n != 1)'),
'pt_BR': ('Portuguese (Brazil)', 2, '(n != 1)'),
'rm': ('Romansh', 2, '(n != 1)'),
'ro': ('Romanian', 3, '(n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2);'),
'ru': ('Russian', 3,
      '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
'sah': ('Yakut', 1, '0'),
'sco': ('Scots', 2, '(n != 1)'),
'si': ('Sinhala; Sinhalese', 2, '(n != 1)'),
'sk': ('Slovak', 3, '(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2'),
'sl': ('Slovenian', 4, '(n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3)'),
'so': ('Somali', 2, '(n != 1)'),
'son': ('Songhai languages', 2, '(n != 1)'),
'sq': ('Albanian', 2, '(n != 1)'),
'sr': ('Serbian', 3,
       '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
'st': ('Sotho, Southern', 2, '(n != 1)'),
'su': ('Sundanese', 1, '0'),
'sv': ('Swedish', 2, '(n != 1)'),
'sw': ('Swahili', 2, '(n != 1)'),
'ta': ('Tamil', 2, '(n != 1)'),
'te': ('Telugu', 2, '(n != 1)'),
'tg': ('Tajik', 2, '(n != 1)'),
'ti': ('Tigrinya', 2, '(n > 1)'),
'th': ('Thai', 1, '0'),
'tk': ('Turkmen', 2, '(n != 1)'),
'tr': ('Turkish', 1, '0'),
'tt': ('Tatar', 1, '0'),
'ug': ('Uighur; Uyghur', 1, '0'),
'uk': ('Ukrainian', 3,
       '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)'),
'vi': ('Vietnamese', 1, '0'),
've': ('Venda', 2, '(n != 1)'),
'wa': ('Walloon', 2, '(n > 1)'),
'wo': ('Wolof', 2, '(n != 1)'),
'yo': ('Yoruba', 2, '(n != 1)'),
# Chinese is difficult because the main divide is on script, not really
# country. Simplified Chinese is used mostly in China, Singapore and Malaysia.
# Traditional Chinese is used mostly in Hong Kong, Taiwan and Macau.
'zh_CN': ('Chinese (China)', 1, '0'),
'zh_HK': ('Chinese (Hong Kong)', 1, '0'),
'zh_TW': ('Chinese (Taiwan)', 1, '0'),
'zu': ('Zulu', 2, '(n != 1)'),
}
"""Dictionary of language data.
The language code is the dictionary key (which may contain country codes
and modifiers).  The value is a tuple: (Full name in English from iso-codes,
nplurals, plural equation).

Note that the English names should not be used in user facing places - it
should always be passed through the function returned from tr_lang(), or at
least passed through _fix_language_name()."""

_fixed_names = {
    "Asturian; Bable; Leonese; Asturleonese": "Asturian",
    "Bokmål, Norwegian; Norwegian Bokmål": "Norwegian Bokmål",
    "Catalan; Valencian": "Catalan",
    "Central Khmer": "Khmer",
    "Chichewa; Chewa; Nyanja": "Chewa; Nyanja",
    "Divehi; Dhivehi; Maldivian": "Divehi",
    "Dutch; Flemish": "Dutch",
    "Filipino; Pilipino": "Filipino",
    "Gaelic; Scottish Gaelic": "Scottish Gaelic",
    "Greek, Modern (1453-)": "Greek",
    "Interlingua (International Auxiliary Language Association)": "Interlingua",
    "Kirghiz; Kyrgyz": "Kirghiz",
    "Klingon; tlhIngan-Hol": "Klingon",
    "Limburgan; Limburger; Limburgish": "Limburgish",
    "Low German; Low Saxon; German, Low; Saxon, Low": "Low German",
    "Luxembourgish; Letzeburgesch": "Luxembourgish",
    "Ndebele, South; South Ndebele": "Southern Ndebele",
    "Norwegian Nynorsk; Nynorsk, Norwegian": "Norwegian Nynorsk",
    "Occitan (post 1500)": "Occitan",
    "Panjabi; Punjabi": "Punjabi",
    "Pedi; Sepedi; Northern Sotho": "Northern Sotho",
    "Pushto; Pashto": "Pashto",
    "Sinhala; Sinhalese": "Sinhala",
    "Sotho, Southern": "Sotho",
    "Spanish; Castilian": "Spanish",
    "Uighur; Uyghur": "Uyghur",
}


cldr_plural_categories = [
        'zero',
        'one',
        'two',
        'few',
        'many',
        'other',
]


def simplercode(code):
    """This attempts to simplify the given language code by ignoring country
    codes, for example.

    .. seealso::

       - http://www.rfc-editor.org/rfc/bcp/bcp47.txt
       - http://www.rfc-editor.org/rfc/rfc4646.txt
       - http://www.rfc-editor.org/rfc/rfc4647.txt
       - http://www.w3.org/International/articles/language-tags/
    """
    if not code:
        return code

    normalized = normalize_code(code)
    separator = normalized.rfind('-')
    if separator >= 0:
        return code[:separator]
    else:
        return ""


expansion_factors = {
        'af': 0.1,
        'ar': -0.09,
        'es': 0.21,
        'fr': 0.28,
        'it': 0.2,
}
"""Source to target string length expansion factors."""

import gettext
import locale
import re
import os

iso639 = {}
"""ISO 639 language codes"""
iso3166 = {}
"""ISO 3166 country codes"""

langcode_re = re.compile("^[a-z]{2,3}([_-][A-Z]{2,3}|)(@[a-zA-Z0-9]+|)$")
langcode_ire = re.compile("^[a-z]{2,3}([_-][a-z]{2,3})?(@[a-z0-9]+)?$",
                          re.IGNORECASE)
variant_re = re.compile("^[_-][A-Z]{2,3}(@[a-zA-Z0-9]+|)$")


def languagematch(languagecode, otherlanguagecode):
    """matches a languagecode to another, ignoring regions in the second"""
    if languagecode is None:
        return langcode_re.match(otherlanguagecode)
    return languagecode == otherlanguagecode or \
           (otherlanguagecode.startswith(languagecode) and \
            variant_re.match(otherlanguagecode[len(languagecode):]))

dialect_name_re = re.compile(r"(.+)\s\(([^)\d]{,25})\)$")
# The limit of 25 characters on the country name is so that "Interlingua (...)"
# (see above) is correctly interpreted.


def tr_lang(langcode=None):
    """Gives a function that can translate a language name, even in the
    form ``"language (country)"``, into the language with iso code langcode,
    or the system language if no language is specified."""
    langfunc = gettext_lang(langcode)
    countryfunc = gettext_country(langcode)

    def handlelanguage(name):
        match = dialect_name_re.match(name)
        if match:
            language, country = match.groups()
            return "%s (%s)" % (_fix_language_name(langfunc(language)),
                                 countryfunc(country))
        else:
            return _fix_language_name(langfunc(name))

    return handlelanguage


def _fix_language_name(name):
    """Identify and replace some unsightly names present in iso-codes.

    If the name is present in _fixed_names we assume it is untranslated and
    we replace it with a more usable rendering.  If the remaining part is long
    and includes a semi-colon, we only take the text up to the semi-colon to
    keep things neat."""
    if name in _fixed_names:
        return _fixed_names[name]
    elif len(name) > 11:
        # These constants are somewhat arbitrary, but testing with the Japanese
        # translation of ISO codes suggests these as the upper bounds.
        split_point = name[5:].find(';')
        if split_point >= 0:
            return name[:5+split_point]
    return name


def gettext_lang(langcode=None):
    """Returns a gettext function to translate language names into the given
    language, or the system language if no language is specified."""
    if not langcode in iso639:
        if not langcode:
            langcode = ""
            if os.name == "nt":
                # On Windows the default locale is not used for some reason
                t = gettext.translation('iso_639',
                                        languages=[locale.getdefaultlocale()[0]],
                                        fallback=True)
            else:
                t = gettext.translation('iso_639', fallback=True)
        else:
            t = gettext.translation('iso_639', languages=[langcode],
                                    fallback=True)
        iso639[langcode] = t.ugettext
    return iso639[langcode]


def gettext_country(langcode=None):
    """Returns a gettext function to translate country names into the given
    language, or the system language if no language is specified."""
    if not langcode in iso3166:
        if not langcode:
            langcode = ""
            if os.name == "nt":
                # On Windows the default locale is not used for some reason
                t = gettext.translation('iso_3166',
                                        languages=[locale.getdefaultlocale()[0]],
                                        fallback=True)
            else:
                t = gettext.translation('iso_3166', fallback=True)
        else:
            t = gettext.translation('iso_3166', languages=[langcode],
                                    fallback=True)
        iso3166[langcode] = t.ugettext
    return iso3166[langcode]


def normalize(string, normal_form="NFC"):
    """Return a unicode string in its normalized form

       :param string: The string to be normalized
       :param normal_form: NFC (default), NFD, NFKC, NFKD
       :return: Normalized string
    """
    if string is None:
        return None
    else:
        import unicodedata
        return unicodedata.normalize(normal_form, string)


def forceunicode(string):
    """Ensures that the string is in unicode.

       :param string: A text string
       :type string: Unicode, String
       :return: String converted to Unicode and normalized as needed.
       :rtype: Unicode
    """
    if string is None:
        return None
    from translate.storage.placeables import StringElem
    if isinstance(string, str):
        #encoding = getattr(string, "encoding", "utf-8")
        #string = string.encode(encoding)
        string = string
    elif isinstance(string, StringElem):
        string = str(string)
    if isinstance(string, bytes):
        string=string.decode('utf-8')
    return string


def normalized_unicode(string):
    """Forces the string to unicode and does normalization."""
    return normalize(forceunicode(string))


def normalize_code(code):
    if not code:
        return code
    return code.replace("_", "-").replace("@", "-").lower()


__normalised_languages = set(normalize_code(key) for key in list(languages.keys()))


def simplify_to_common(language_code, languages=languages):
    """Simplify language code to the most commonly used form for the
    language, stripping country information for languages that tend
    not to be localized differently for different countries"""
    simpler = simplercode(language_code)
    if simpler == "":
        return language_code

    if (normalize_code(language_code) in __normalised_languages):
        return language_code
    else:
        return simplify_to_common(simpler)

def get_language(code):
    code = code.replace("-", "_").replace("@", "_").lower()
    if "_" in code:
        # convert ab_cd → ab_CD
        code = "%s_%s" %(code.split("_")[0], code.split("_", 1)[1].upper())
    return languages.get(code, None)
