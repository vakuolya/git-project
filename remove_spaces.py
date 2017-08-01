def remove_spaces1(n):
    return n.replace(" ", "")

print remove_spaces1("S tr    ing ")


def remove_spaces2(n):
    return "".join(n.split())

print remove_spaces2("S tr    ing ")


import re
def remove_spaces3(n):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', n)

print remove_spaces3("S tr    ing ")


def remove_spaces4(n):
    s = []
    for i in n:
        if ord(i) != 32:
            s.append(i)
    return "".join(s)

print remove_spaces4("S tr    ing ")
