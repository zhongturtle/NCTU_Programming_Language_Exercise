lines = [line.rstrip('\n') for line in open('xy.txt')]
#print(lines)

upper_num = lines[0] 
lower_num = lines[1]
#print(upper_num)
#print(lower_num)
#test = 3
#i = 1
upper_sum = 1
lower_sum = 1
for i in range(int(upper_num) - int(lower_num) + 1,int(upper_num)+1):
    upper_sum = upper_sum * i
    #print(str(i) + ":" + str(upper_sum))
	
for i in range(1,int(lower_num)+1):
    lower_sum = lower_sum * i
    #print(str(i) + ":" + str(lower_sum))
	
print("C : " + str(upper_sum / lower_sum))
print("P : " + str(upper_sum)) 
