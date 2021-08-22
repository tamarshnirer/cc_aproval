def num_to_years(num):
    try:
        if num < 0:
            year = num/-365
        else:
            year = 0
    except:
        return None
    return year

def status_int(s):
    if s=='C':
        return 1
    if s=='X':
        return 2
    else:
        return s

