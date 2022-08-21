from functools import partial as p
import re

ensure_space_after_comma = p(re.sub, r"(?<=,)(?=\S)", " ")
ensure_no_space_before_comma = p(re.sub, r"\s+,", ",")

replace_newline = p(re.sub, r"\n", " ")
replace_space = p(re.sub, r"\xa0", " ")
deduplicate_spaces = p(re.sub, r"\s{2,}", " ")



def preprocess(t: str) -> str:
    """
    Normalizes whitespaces and replaces bad characters
    """
    functions = [
        ensure_space_after_comma,
        ensure_no_space_before_comma,
        replace_newline,
        replace_space,
        deduplicate_spaces,
        str.strip,
    ]
    for func in functions:
        t = func(t)
    return t