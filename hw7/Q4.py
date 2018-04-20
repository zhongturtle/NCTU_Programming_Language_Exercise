def draw_graph(n):
    graph = ""

    for i in range(0 , n - 1):
       line = ""
       #for j in range(0 , n - i -1):
       #    line = line + " "
       line = line + " " * (n - i -1)
       line = line + "*"
       #for j in range(0 , 2 * i - 1):
       #    line = line + " "
       line = line + "+" * (2 * i -1)

       line = line + "*\n"
       graph = graph + line
    graph = graph.replace("**" ,"*")

    graph = graph + "*" * (n * 2 - 1)

    print(graph)

draw_graph(7)