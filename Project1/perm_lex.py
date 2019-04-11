def perm_gen_lex(a):
    a = list(a)
    newlist = []
    if len(a) == 1:
        return a
    if len(a) == 0:
        return a
    else:
        for char in range(len(a)):
            first = a[char]
            rest = a[:char] + a[char + 1:]
            for order in perm_gen_lex(rest):
                newlist.append(first + order)
        return newlist
 
