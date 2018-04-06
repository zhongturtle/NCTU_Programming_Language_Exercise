my_file = open("dna.txt")
content = my_file.read()
my_file.close
#print(content)
total_len = len(content)
#print(total_len)
A_content_len = content.count("A")
T_content_len = content.count("T")
AT_content_len = A_content_len + T_content_len
AT_ratio = AT_content_len/total_len

print("AT content : " + str(AT_ratio)) 
