amino_acid_file = open("amino_acid_codes.txt")
amino_acid_info = amino_acid_file.read()
amino_acid_file.close()
line_num = 0
is_decribe = 0
info = ""
for word in amino_acid_info:
    if word == "#":
	    is_decribe = 1
    elif word == "\n":
	    is_decribe = 0
	    #print("aa")
    if is_decribe == 0:
        #print(word , end = "")
        info = info + word
    else:
	    word.replace(word , "a")
    #line_num = line_num + 1
#print(amino_acid_info)
#info[0] = ""
#info[1] = ""
#info[2] = ""
print(info)
#print(info.replace("\n", "").split("\t"))
