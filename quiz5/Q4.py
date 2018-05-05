Numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20] 

#def selection_sort(list):
#    lenth = len(list)
#    max_num = max(list)
#	max_num_dict = list.find(max_num)
#	tem = list[length - 1]
#	list[length - 1] = max_num
#	list[max_num_dict] = tem
#	return 

i = len(Numbers)	
while i > 0:
    max = 0
    for x in range(0 , i):
	    if x > max:
		    max = x
	