num_heads = 1000
num_legs  = 3330
h = 0
c = 0

for h in range(0, num_heads+1):
    c  = num_heads - h
    if 4*h + 2*c == num_legs:
       ans_found = True
       break

print(h, "horses,", c, "chickens")