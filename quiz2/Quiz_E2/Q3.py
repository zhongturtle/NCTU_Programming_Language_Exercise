my_file = open("xy.txt")
content = my_file.read()
my_file.close()
upper_num = content[0:2] 
lower_num = content[3]
#print(upper_num)
#print(lower_num)
#test = 3
#i = 1
upper_sum = 1
lower_sum = 1
for i in range(int(lower_num),int(upper_num)+1):
    upper_sum = upper_sum * i
    #print(str(i) + ":" + str(upper_sum))
	
for i in range(1,int(lower_num)+1):
    lower_sum = lower_sum * i
    #print(str(i) + ":" + str(lower_sum))
	
print("C : " + str(upper_sum / lower_sum))
print("P : " + str(upper_sum)) 