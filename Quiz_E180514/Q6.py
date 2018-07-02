#def distant_count(height,time):
#    if time > 0:
#        return height*2 + 2 * distant_count(height/2,time)
#    else:
#	    return 0
		

height = 100
#print(distant_count(100/2,2))
sum = 0
for i in range(0, 9):
    height = height / 2
    sum = sum + height * 2
	
sum = sum + 100
print(sum)