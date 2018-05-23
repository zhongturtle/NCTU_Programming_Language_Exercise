### Obtain mushroom data
Heights = {}
GrowthRates = {}

file_mushroom_data = open("mushrooms_heights.txt")

for line in file_mushroom_data:
    Data = line.strip("\n").split("\t")
    Heights[ Data[0] ] = float(Data[1])
    GrowthRates[ Data[0] ] = float(Data[2])

file_mushroom_data.close()

#print(Heights)
#print(GrowthRates)


### Compute heights
for day in range(1, 3+1):
    for mushroom, height in Heights.items():
        Heights[mushroom] += Heights[mushroom] * GrowthRates[mushroom]/100
        if Heights[mushroom] > 20: Heights[mushroom] = 0


### Output
for mushroom in sorted(Heights.keys()):
    height = round(Heights[mushroom], 1)
    print("Mushroom " + mushroom + "\t" + str(height))
