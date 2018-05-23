num_heads = 262
num_legs  = 846
num_horns = 197
num_wings = 212

horses, dears, unicorns, chickens = 0, 0, 0, 0

answered = False
heads_sum = 0
for horses in range(0, num_heads+1):
    heads_sum = horses
    for dears in range(0, num_heads-heads_sum+1):
        heads_sum = horses + dears
        for unicorns in range(0, num_heads-heads_sum+1):
            heads_sum = horses + dears + unicorns
            chickens = num_heads - heads_sum

            if chickens < 0: break

            if 4*horses + 4*dears + 4*unicorns + 2*chickens == num_legs \
               and 2*dears + unicorns == num_horns \
               and 2*unicorns + 2*chickens == num_wings:
                answered = True
                break

        if answered: break
    if answered: break

print(horses, dears, unicorns, chickens)