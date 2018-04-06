my_file = open("dna.txt")
content = my_file.read()

total_len = len(content)
#print(total_len)
AT_content_len = content.count("AT")

AT_ratio = AT_content_len/total_len

print("AT content : " + str(AT_ratio)) 