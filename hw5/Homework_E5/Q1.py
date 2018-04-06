n = 5
graph = ""

for i in range(0 , n):
    line = ""
    for j in range(0 , n - i -1):
        line = line + " "
    line = line + "*"
    for j in range(0 , 2 * i - 1):
        line = line + " "
    line = line + "*\n"
    graph = graph + line

for i in range(0 , n -1):
    line = ""
    for j in range(0 , i + 1):
        line = line + " "
    line = line + "*"
    for j in range(0 , 2*(n - i -2) - 1):
        line = line + " "
    line = line + "*\n"
    graph = graph + line

graph = graph.replace("**" ,"*")
#print(graph.count("**"))

print(graph)