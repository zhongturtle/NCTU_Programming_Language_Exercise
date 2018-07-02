distance_total = 0
height = 100

distance_total += height
t = 0
while t<11:
  t += 1
  print("Before bounce", t, "=>", distance_total)

  height *= 0.5
  distance_total += height * 2
