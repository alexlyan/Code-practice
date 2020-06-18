def partially_hide(s):
    return ' '.join(x[0]+'-'*(len(x)-2)+x[-1] for x in s.split())

