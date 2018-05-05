Numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def selection_sort(list):
    for i in range(len(list)):
        mini = min(list[i:]) #find minimum element
        min_index = list[i:].index(mini) #find index of minimum element
        list[i + min_index] = list[i] #replace element at min_index with first element
        list[i] = mini                  #replace first element with min element
        print(list)


#print (source)
print("Number : ", Numbers)
print()
print("Selection sorting : ")
selection_sort(Numbers)
print()
print("Final result : ")
print(Numbers)