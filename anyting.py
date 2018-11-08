"""words = ['kata','papa','anya', 'zsiga', 'csiga',]
sortedwords = []
paceholder = words[0]
i = 0
for word in words:
    print(word)
    if paceholder[0] > words[i][0]:
        sortedwords.insert(0,word)
    else:
        sortedwords.append(word)
    i +=1
print(sortedwords)"""


   

def sort_abc(str1, str2):
    if str2.startswith(str1) and len(str1) < len(str2):
        return True
    elif str1.startswith(str2) and len(str2) < len(str1):
        return False
    if str1[0] == str2[0]:
        return sort_abc(str1[1:], str2[1:])
    else:
        return str1[0] < str2[0]

sort_abc('anya','kapa')