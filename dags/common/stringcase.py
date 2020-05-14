import re


def lowercase(string):
    return str(string).lower()


def snake_case(string):
    if not string:
        return string
    string = str(string)
    string = re.sub(r"[A-Z]+", lambda matched: "_" + matched.group(0), string)
    string = re.sub(r"[_\-.\s]+", "_", string)
    return lowercase(string.strip("_"))


def kebab_case(string):
    if not string:
        return string
    string = str(string)
    string = re.sub(r"[A-Z]+", lambda matched: "-" + matched.group(0), string)
    string = re.sub(r"[_\-.\s]+", "-", string)
    return lowercase(string.strip("-"))
