matrix = ""
for x in range(1, 9+1):
    for y in range(1, x+1):
        matrix += str(x) + "x" + str(y) + "=" + str(x*y) + "\t"
    matrix += "\n"

print(matrix)