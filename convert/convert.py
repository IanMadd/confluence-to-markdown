import re
import pandoc
from pandoc.types import *
from convert.config import *


def read(file_path, format):
    """input HTML and return a pandoc doc object"""
    pandoc_doc = pandoc.read(source=None, file=file_path, format=format)
    return pandoc_doc


def uppercase(doc):
    """Convert strings to uppercase"""
    for elt in pandoc.iter(doc):
        if isinstance(elt, Str):
            elt[0] = elt[0].upper() # elt: Str(Text)

def pandoc_object_processing(doc_object):
    """Process pandoc object to remove certain sections of text"""
    for elt, path in pandoc.iter(doc_object, path=True):
        if elt == 'breadcrumb-section':
            del_path = path[-3]
            holder, index = del_path
            del holder[index]

    for elt, path in pandoc.iter(doc_object, path=True):
        if elt == 'page-metadata':
            #print(path[-3])
            del_path = path[-4]
            holder, index = del_path
            del holder[index]

    for elt, path in pandoc.iter(doc_object, path=True):
        if elt == 'footer':
            # print(path[-2])
            del_path = path[-3]
            holder, index = del_path
            del holder[index]

    return doc_object