def BMI_caculate(weight , height):
    bmi = weight / (height * height)
    return bmi

weight = 70
height = 1.75

print("Weight(kg) : " + str(weight))
print("Height(m) : " + str(height))
print("BMI : " + str(BMI_caculate(weight , height))) 