import bisect

def contains(t, aa):
    # https://docs.python.org/3/library/bisect.html
    """
    input: aa is a sorted list
    output: True iif t is in aa
    algo uses binary search
    """
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(aa, t)
    if i != len(aa) and aa[i] == t:
        return True
    return False