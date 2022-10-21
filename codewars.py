def inner(length, minimum, maximum, s):
    if minimum == maximum:
        return s.append(str(minimum))
    s.append(str(minimum))
    inner(length, minimum + 1, maximum, s)
    s.append(str(minimum))
    return s
def ascend_descend(length, minimum, maximum):
    s = []
    if minimum == maximum:
        return length * str(minimum)
    elif length == 0 or maximum < minimum:
        return ''
    else:
        res = inner(length, minimum, maximum, s)
        if len(res) < length:
            a = res[:-1]
            while len(a) < length:
                a *= 2
            return "".join(a)[:length]
        else:
            return "".join(res)[:length]


print(ascend_descend(4, 0, 5))
