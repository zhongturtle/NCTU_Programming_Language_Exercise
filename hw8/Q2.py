numbers = [50.9, 50.3, 48.7, 89.2, 60.0, 74.0, 54.2, 101.6, 84.9, 82.1, 79.4, 93.8]
#print("numbers = " + str(numbers))

def my_medium(list):
    list_length = len(list)
    #print(list_length)
    list.sort()
    #print(numbers)
    #print(int(3/2))
    num_1 = list[int(list_length / 2)]
    #print(int(list_length / 2) -1)
    list.reverse()
    num_2 = list[int(list_length / 2)]
    #print(int((list_length + 1) / 2) -1)
    medium = (num_1 + num_2) / 2
    
    return medium

assert my_medium(numbers) == 76.7
assert my_medium([1, 3, 5, 10, 20]) == 5
print("my_medium([1, 3, 5, 10, 20]) ： " + str(my_medium([1, 3, 5, 10, 20])))
print()
print("numbers = " + str(numbers))
print("my_medium(numbers) : " + str(my_medium(numbers)))