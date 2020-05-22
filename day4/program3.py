n = int(input(" Enter the number of elements of dictionry : "))
d =dict()
l = [ tuple(input(' Enter key and value : ').split()) for i in range(n)]
dic = dict(l)

val_dic = list(dic.values())
val_dic.sort(reverse = True)
print(" Second Maximum value : ",val_dic[1])
