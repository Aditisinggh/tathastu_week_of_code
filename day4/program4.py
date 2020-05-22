n = int(input(" Enter the number of elements of dictionry : "))
d =dict()
l = [ tuple(input(' Enter key and value : ').split()) for i in range(n)]
dic = dict(l)

val_dic = dic.values()
print(' All values of dictionary : ' , val_dic)

print(' Distinct values of dictionary : ' , set(val_dic))
