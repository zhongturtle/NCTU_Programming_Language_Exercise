matrix = ""
for i in range(0 , 10):
    matrix = matrix + str(i) + "\t"
matrix = matrix.replace("0" , " ")
matrix = matrix + "\n"
#print(matrix)

for i in range(1 , 10):
    matrix = matrix + str(i) + "\t"
    for j in range(1 , 10):
        matrix_unit = i * j
        matrix = matrix + str(matrix_unit) + "\t"
    matrix = matrix + "\n"

print(matrix)
