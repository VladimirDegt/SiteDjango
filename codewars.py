from re import findall
def string_expansion(s):
    if not s or s.isdigit():
        return ''
    elif s.isalpha():
        return s
    else:
        res = ''
        expreg = findall(r"\d[A-Za-z]+", s)
        expreg_start = findall(r'^[A-Za-z]+', s)
        if len(expreg_start):
            res += expreg_start[0]
            for elem in expreg:
                if len(elem) == 2:
                    elem = int(elem[0]) * elem[1]
                    res += elem
                else:
                    for i in range(1, len(elem)):
                        res += (int(elem[0]) * elem[i])
            return res
        else:
            for elem in expreg:
                if len(elem) == 2:
                    elem = int(elem[0]) * elem[1]
                    res += elem
                else:
                    for i in range(1, len(elem)):
                        res += (int(elem[0]) * elem[i])
            return res
print(string_expansion('A4g1b4d'))