numbers = [50.9, 50.3, 48.7, 89.2, 60.0, 74.0, 54.2, 101.6, 84.9, 82.1, 79.4, 93.8]
print("numbers = " + str(numbers))

def my_medium(list):
    list_length = len(numbers)
    #print(list_length)
    numbers.sort()
    #print(numbers)
    #print(int(3/2))
    num_1 = numbers[int(list_length / 2)]
    #print(int(list_length / 2) -1)
    numbers.reverse()
    num_2 = numbers[int(list_length / 2)]
    #print(int((list_length + 1) / 2) -1)
    medium = (num_1 + num_2) / 2
    
    return medium

assert my_medium(numbers) == 76.7

print("Medium : " + str(my_medium(numbers)))