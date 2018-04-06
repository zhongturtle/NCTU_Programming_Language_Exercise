my_file = open("animals.txt")
animal_list = my_file.read()
my_file.close()

animal_list.sort()

print(animal_list)