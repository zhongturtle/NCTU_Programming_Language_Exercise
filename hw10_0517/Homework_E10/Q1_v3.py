def cal_number(num_heads, num_legs):
    for h in range(num_heads + 1):
        c = num_heads - h
        if 4*h + 2*c == num_legs: return h, c

numheads = 1000
numlegs = 3330
h, c = cal_number(numheads, numlegs)

print(h, "horses,", c, "chickens")