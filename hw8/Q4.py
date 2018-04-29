list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def bubble_sort_flag(list):
    for i in range(0 , len(list) - 1):
        flag = False
        for j in range(0 , len(list) - 1 - i):
            if list[j] > list[j+1]:
                flag = True
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
        if flag == False:
            break
        print("pass" , i + 1 , ": " , list)

print("Original list : " + str(list))
print()
bubble_sort_flag(list)
print()
print("Final list : " + str(list))
