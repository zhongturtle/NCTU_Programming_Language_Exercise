def strLen(string):
    if string == '':
	    return 0
    else:
        string = string[0: -1]
        print(string)
        return 1 + strLen(string)

assert strLen("ABCDE") == 5
assert strLen("13579246810") == 11
assert strLen("") == 0		

#string = "ABCDE"
#print(string)
#print()
#print(strLen(string))