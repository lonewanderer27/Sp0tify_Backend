import re, string

# STRING STUFF
def remove_punctuation(s):
    no_punc = str.maketrans('', '', string.punctuation)
    return s.translate(no_punc)

def remove_extra_spaces(s):
    return ' '.join(s.split())

def remove_apostrophe(s):
    return s.replace('’', '')

def replace_apostrophe(s):
    return s.replace('’', "'")

def remove_zero_width_space(s):
    return s.replace('\u200b', '')

def remove_right_to_left_mark(s):
    return s.replace('\u200f', '')

def scrub_string(s):
    '''
    Removes opinionated unwanted characters from 
    string, namely:
        - zero width spaces '\u200b' ---> ''
        - apostrophe '’' ---> ''
        - extra spaces '    ' ---> ' '
    '''
    s = remove_zero_width_space(s)
    s = remove_right_to_left_mark(s)
    s = remove_apostrophe(s)
    s = remove_extra_spaces(s)
    return s


def replace_br(s):
    s = s.replace('<br/>', '\n')
    return s

def keep_until(s, substr, case_insensitive=False):
    # Look for substr index and slice
    if case_insensitive:
        try:
            index = s.lower().index(substr.lower())
            return s[:index]
        except ValueError:
            # NOTE: index not found
            return s
        
    # Just split and take first
    until, *after_ = s.split(substr)[0]
    return until

def remove_until(s, substr, case_insensitive=False):
    # Look for substr index and slice
    if case_insensitive:
        try:
            index = s.lower().index(substr.lower())
            return s[index:]
        except ValueError:
            # NOTE: index not found
            return s
        
    # Just split and take second
    until, *after_ = s.split(substr)[0]
    return until


def until_embded(s, case_insensitive=False, use_regex=True):
    if use_regex:
        pattern = f"Embed\d+\b"
        found = re.findall(pattern, s,  flags=re.IGNORECASE)
        for f in found:
            s.replace(f, '')
        return s
    else:
        s = keep_until(s, 'Embed', case_insensitive=case_insensitive)
        # NOTE: could be Embed1, Embed27, etc
        if s != '':
            while s[-1].isnumeric():
                s = s[:-1]
        return s
    return s

def remove_see_live_ad(s, include_word_boundaries=True):
    pattern = r"\bSee .+ Live\b" if include_word_boundaries else r"See .+ Live"
    ads = re.findall(pattern, s,  flags=re.IGNORECASE)
    for ad in ads:
        s = s.replace(s, '')
    return s

def remove_square_brackets(s):
    pattern = r"\[([A-Za-z0-9_]+)\]"
    brackets = re.findall(pattern, s,  flags=re.IGNORECASE)
    for found in brackets:
        s.replace(found, '')
    return s