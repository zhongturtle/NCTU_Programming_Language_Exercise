seq = "If two witches would watch two watches, which witch would watch which watch?"

seq = seq.replace("." , "").replace("," , "").replace("?" , "").replace(";" , "")
words = seq.split(" ")
#type = seq.split(" ")
word_classes = []
for i in words:
    if i not in word_classes : 
        word_classes.append(i)
print(word_classes)
#for i in range(0 , len(type)):
#    for j in range(i , len(type)):
#        if type[i] == type[j]:
#            type.remove(type[j])
            
#print(words)
#print(type)
print("Word", "\t" , "Occurrence")
word_classes.sort()
num = 0
for i in word_classes:
    print(i , "\t", words.count(i))
    #if(i == type[num - 1]):
	#    num = num + 1 
	#else:
    #    print(i,"\t",seq.count(i))
    #    num = num + 1 