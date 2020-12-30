#The Z algo is used for pattern matching. AND also for other problems

#It creates the Z array in linear time
#Note that the first element of the zarray is always equal to len(ss)

#It allows to find a pattern tt in a string ss in O(len(ss) + len(tt))
#this is quite beautiful result because this is the time needed to read both strings anyway

#Great explanation and demo on these two consecutive videos:
#https://www.youtube.com/watch?v=MFK0WYeVEag
#https://www.youtube.com/watch?v=NVJ_ELSbbew



def z_algorithm(ss):
    """
        Args:
            param1: string ss
            
        Returns:
            a list. At each index i, we have a number corresponding to the longest substring ss[i:i+x]
            which is also a prefix of ss
    """
    res = [0] * len(ss)
    res[0] = len(ss)
    i, j = 1, 0
    while i < len(ss):
        while i + j < len(ss) and ss[j] == ss[i + j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(ss) and k + res[k] < j:
            res[i + k] = res[k]
            k += 1
        i, j = i + k, j - k
    return res


def pattern_matching(ss, tt):
    """
        Args:
            param1: string ss: string that contain a pattern or not
            param2: string tt: pattern
            
        Returns:
            a list of integers. Each integer is an index of ss where there is a match
    """
    assert("$" not in ss and "$" not in tt) #otherwise choose another character 
    new_ss = tt + "$" + ss

    z_array = z_algorithm(new_ss)

    result = []
    for i, zi in enumerate(z_array):
        if i != 0  and zi == len(tt):
            result.append(i - len(tt) - 1)

    return result


#examples

print()
print()
print("##################################")
print("# Example 1 :  calculate Z-array #")
print("##################################")
print()
print()
#If you choose ss = abcababyabcabaabr
#you will get
# --------------------------------------------------------------------
# 17 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 6 | 0 | 0 | 2 | 0 | 1 | 2 | 0 | 0
# --------------------------------------------------------------------
#Note again that the first element of the zarray is always equal to len(ss). It is 17 here.


# ss = input()
ss = "abcababyabcabaabr"
z_array = z_algorithm(ss)

#display answer in a somewhat nice way
print("Nice display:")
print("             ", "-" * len(ss) * 4)
print("input string: ", " | ".join([x for x in ss]))
print("             ","-" * len(ss) * 4)
print("             ","-" * len(ss) * 4)
print("Z-array:     ", " | ".join([str(x) for x in z_array]))
print("             ","-" * len(ss) * 4)
print()

#display answer in a simple way
print("A more simple display of the same Z-array:")
print(" ".join([str(x) for x in z_array]))


print()
print()
print("##################################")
print("# Example 2 :  Pattern matching  #")
print("##################################")
print()
print()


tt = "abc"
ss = "bbcabcbyabcabar"

print("             ", "-" * len(ss) * 5)
print("ss  indexes: ", " | ".join([f"{i:02d}" for i in range(len(ss))]))
print("             ","-" * len(ss) * 5)
print("             ", "-" * len(ss) * 5)
print("ss  string:  ", " | ".join([x+ " " for x in ss]))
print("             ","-" * len(ss) * 5)
print("             ","-" * len(tt) * 4)
print("tt pattern:  ", " | ".join([x + " " for x in tt]))
print("             ","-" * len(tt) * 4)
print()


ans = pattern_matching(ss, tt)
print("Index matches: ", ", ".join([str(x) for x in ans]))


print()
print()
print("#########################################")
print("# Example 2 :  Is tt a rotation of ss?  #")
print("#########################################")
print()
print()

#we just need to search if tt is in ss + ss

ss = "abcde"
tt = "cdeab"
print("First example: ")
print("             ", "-" * len(ss) * 5)
print("ss  indexes: ", " | ".join([f"{i:02d}" for i in range(len(ss))]))
print("             ","-" * len(ss) * 5)
print("             ", "-" * len(ss) * 5)
print("ss  string:  ", " | ".join([x+ " " for x in ss]))
print("             ","-" * len(ss) * 5)
print("             ","-" * len(tt) * 4)
print("tt pattern:  ", " | ".join([x + " " for x in tt]))
print("             ","-" * len(tt) * 4)
print()


ans = pattern_matching(ss + ss, tt)
if ans:
    print("'"+tt+"'", "is a rotation of", "'"+ss+"'", "?: Yes")
else:
    print("'"+tt+"'","is a rotation of","'"+ss+"'", "?: No")
print()
print()
ss = "abcdf"
tt = "cdeab"
print("Second example: ")
print("             ", "-" * len(ss) * 5)
print("ss  indexes: ", " | ".join([f"{i:02d}" for i in range(len(ss))]))
print("             ","-" * len(ss) * 5)
print("             ", "-" * len(ss) * 5)
print("ss  string:  ", " | ".join([x+ " " for x in ss]))
print("             ","-" * len(ss) * 5)
print("             ","-" * len(tt) * 4)
print("tt pattern:  ", " | ".join([x + " " for x in tt]))
print("             ","-" * len(tt) * 4)
print()


ans = pattern_matching(ss + ss, tt)

if ans:
    print("'"+tt+"'", "is a rotation of", "'"+ss+"'", "?: Yes")
else:
    print("'"+tt+"'","is a rotation of","'"+ss+"'", "?: No")
print()
print()

print()
print()
print("##################################")
print("# Other examples :               #")
print("##################################")
print()
print()

print(" - Codeforces:  Educational Codeforces Round 101 (Rated for Div. 2), Problem E")

