def median(numbers):
    numbers.sort()
    num_numbers = len(numbers)

    if num_numbers%2 == 1:
       return numbers[ int((num_numbers-1) / 2) ]
    else:
       return ( numbers[ int(num_numbers / 2) ] + numbers[ int((num_numbers-2) / 2) ] ) /2



##### Main Program
numbers = [1, 3, 5]
numbers = [1, 2, 3, 5]

print("Numbers:")
print(numbers)
print()
print("The median = " + str(median(numbers)))