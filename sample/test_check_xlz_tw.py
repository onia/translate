#!/usr/bin/env python

"""Tests for the zip storage module"""

import os
import re
from zipfile import ZipFile
from collections import OrderedDict

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


def check_xlz_units(Test_path):
    """Tests basic functionality."""
    for root, dirs, files in os.walk(Test_path):
        for xlz_file in files:
            # get the full path of the file
            original_full_path_file=os.path.join(root, xlz_file)
            # get the xlz file
            if re.search('\.xlz$',xlz_file):
                print(xlz_file)
                testdata=[]
                d = zipw.ZIPFile(original_full_path_file, 'xlf')
                stdchecker = checks.StandardChecker(checks.CheckerConfig(targetlanguage='zh'))
                count=-1
                #prevUnitLocation=None
                #currentUnitLocation=None
                for unit in d.getunits():
                    if unit.source==None: continue
                    if unit.target==None:
                        if unit.istranslatable():                   
                            testdata.append(unit.source+'\n')
                        continue
                    if fails(stdchecker.numbers, unit.source, unit.target):
                        testdata.append(unit.source+'\t'+unit.target+'\n')
                    #print(unit.source)
                    #unit.target=unit.source
                    #testdata.append(unit.target)
                    #unit.setmetadata(translation_status='finished')
                    #if not unit.source or not unit.target: continue
                    #if fails(stdchecker.endpunc, unit.source, unit.target):
                    #print(unit.getlocations(), unit.source.encode('utf-8'), unit.target.encode('utf-8'), unit.get_state_n(), unit.getid())
                    #print(unit.source)
                    #if unit.target:
                       #print(unit.source.encode('utf-8'))
                    #unit.setmetadata(translation_status='finished')
                    #if unit.getmetadata()['match-quality']=='guaranteed':
                    #   unit.setmetadata(lock_status='locked')
                    #print(unit.source)
                    #if str(unit.source).count('Failed to load {46}'):
                    #    print(unit.source)
                    #    unit.target='Failed to load {46}'
                    #    unit.setmetadata(translation_type='manual_translation')
                    #if count>100:
                    #    break
                    #print(unit.getmarkupdata())
                    '''
                    currentUnitLocation=unit.getid()
                    if prevUnitLocation!=currentUnitLocation:
                        count+=1
                        testdata.append({})
                    testdata[count][str(unit.getunitid())]=unit.source
                    testdata[count].update(unit.getmarkupdata())
                    prevUnitLocation=currentUnitLocation
                    '''
                if testdata!=[]:
                    #testdata=[OrderedDict(sorted(dic.items(), key=lambda t: t[0])) for dic in testdata]
                    f=open(original_full_path_file+'.txt','w', encoding='utf-8')
                    '''for dic in testdata:
                        for ky in dic:
                            f.write(dic[ky].replace('\n',''))
                    '''
                    for item in testdata:
                        f.write(item)
                    f.close()
                    #for subdir, file in d.getfiles():
                    #    print(type(file))
                    #d.savefiles()


if __name__=='__main__':
    Test_path=os.getcwd()
    check_xlz_units(Test_path)
