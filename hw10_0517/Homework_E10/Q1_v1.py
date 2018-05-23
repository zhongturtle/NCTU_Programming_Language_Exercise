num_heads = 1000
num_legs  = 3330
h = 0
c = 0

ans_found = False
for h in range(0, num_heads+1):
    for c in range(0, num_heads-h+1):
        if 4*h + 2*c == num_legs:
           ans_found = True
           break
    if ans_found: break

print(h, "horses,", c, "chickens")