words = "If two witches would watch two watches, which witch would watch which watch?"
print(words)
words = words.replace(",", "").replace("?", "")
words = words.split(" ")
#print(words)
def make_diction(words):
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = words.count(word)
    key = dict.keys()
    #key.sort()
    #print(key)
    #print(sorted(dict.keys()))
    return dict

#print(make_diction(words))
word_dict = make_diction(words)
word_keys = sorted(word_dict.keys())
print("Word", "\t", "Frequency")
#print(word_dict)
for i in word_keys:
    print(i , "\t" , word_dict[i])
