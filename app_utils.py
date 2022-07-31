#strip special chars with the exception of _
#tokenize
#word count/frequency


import re
import keyword
import builtins
from collections import defaultdict

def strip_special_chars(docx):
    # new_string = re.sub(r"[a-zA-Z0-9]","",docx)
    new_string = re.sub(r"\W+"," ",docx)
    return new_string


def get_reserved_word_frequency(docx):
    cleaned_docx = strip_special_chars(docx)
    reserved_keyword_dict = defaultdict(int)
    identifier_dict = defaultdict(int)
    builtins_dict = defaultdict(int)
    for i in cleaned_docx.split(): # tokenized
        if i in keyword.kwlist:
            reserved_keyword_dict[i] += 1
        elif i in list(dir(builtins)):
            builtins_dict[i] +=1
        else:
            identifier_dict[i] +=1

    results = {"reserved":reserved_keyword_dict,"identifiers":identifier_dict,"builtins":builtins_dict}
    return results







    