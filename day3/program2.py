from itertools import permutations as p

s = input(" String : ")
per = p(s)

print(" Permutations :", end = ' ')
for i in per :
    print(''.join(i) , end = ' ')
