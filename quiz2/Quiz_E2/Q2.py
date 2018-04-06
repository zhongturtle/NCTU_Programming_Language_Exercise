numbers = [164.9, 150.3, 148.7, 189.2, 160.0, 174.3, 154.2, 201.6, 184.9,
182.1, 179.4, 193.8]

##the_min = 200
numbers.sort()

sum = 0
##print(sum)
for number in numbers:
    sum = sum + number
avarage = sum / 12	
#print(sum)

median = ( numbers[5] + numbers[6] ) / 2

#print(median)
print("The minimum is : " + str(numbers[0]))
print("The maximum is : " + str(numbers[11]))
print("The avarage is : " + str(avarage))
print("The median is : " + str(median))
