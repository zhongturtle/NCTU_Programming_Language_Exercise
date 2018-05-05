num = int(input("Please input a number: "))

list = []
i = 2
while i <= num : 
    is_prime = True
    j = 2
    while j < i:
        if(i % j == 0):
            is_prime = False
            break
        else:
            is_prime = True
        j = j + 1
    if(is_prime == True):
        list.append(i)
    i = i + 1	
print("Prime number <= ",num," are listed here: ")
count = 0
#for i in list:
    #print(i , endswith(""))
print(list)
    #count = count + 1
print("Number of primes: " , len(list))