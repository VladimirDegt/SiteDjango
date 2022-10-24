from collections import Counter
from string import ascii_lowercase
def is_pangram(s):
    d1 = Counter(ascii_lowercase)
    d2 = Counter(s.lower())
    d3 = d2.copy()
    for elem in d2:
        if not elem.isalpha():
            del d3[elem]
    return len(d1) == len(d3)

print(is_pangram("The quick brown fox jumps over the lazy dog"))