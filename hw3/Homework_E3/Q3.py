my_file = open("blood_pressures.txt")
content = my_file.read()
my_file.close()

num_1 = int(content[0:3])
num_2 = int(content[5:8])
num_3 = int(content[10:13])
num_4 = int(content[15:18])
num_5 = int(content[20:23])
num_6 = int(content[25:28])
num_7 = int(content[30:33])

pressure_total = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7
pressure_average = pressure_total / 7
print("The average of blood pressure is : " + str(pressure_average))
