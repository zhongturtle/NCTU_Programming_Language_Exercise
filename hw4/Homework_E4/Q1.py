my_file = open("animals.txt")
animal_list = my_file.read()
my_file.close()

animal_list = animal_list.split("\n")
animal_list.sort()
animal_list.reverse()
for i in animal_list:
    print(i)

#print(animal_list)
