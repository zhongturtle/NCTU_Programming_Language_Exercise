horse_num = 0
chicken_num = 1000

for i in range(0 , 1000):
    horse_num = horse_num + 1
    chicken_num = chicken_num - 1
    total_feet = horse_num * 4 + chicken_num *2
    if total_feet == 3330:
	    #print("found it")
	    print("num of horse : ",horse_num)
	    print("num of chicken : ", chicken_num)