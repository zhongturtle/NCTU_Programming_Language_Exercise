upper_num = [5]
lower_num = [3]
#print(upper_num)
#print(lower_num)

for i in range(1 , 21):
    lower_num.append(upper_num[i-1] + 2)
    upper_num.append(upper_num[i-1] * 2 + lower_num[i-1])	
#print(upper_num)
#print(lower_num)
#print(len(upper_num))
#print(len(lower_num))
sum = 0

for i in range(0 , 20):
    fraction = upper_num[i] / lower_num[i]
    #print(fraction)
    sum = sum + fraction
print("Sum : " + str(sum))