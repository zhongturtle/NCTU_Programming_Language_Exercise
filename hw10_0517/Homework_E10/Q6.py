def strLen(str):
    len = 0
    for ch in str: len += 1
    return len



##### Main Program
assert strLen("ABCDE") == 5
assert strLen("13579246810") == 11
assert strLen("") == 0
