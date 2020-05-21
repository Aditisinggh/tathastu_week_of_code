s = input( " String : ")                #original string
string = str()
for i in range(len(s)) :
    if s[i] not in string :
        string += s[i]
s = string
print(" Modified String : " , s)        #string after duplicates removal
