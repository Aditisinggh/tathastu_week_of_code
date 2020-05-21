l1 = input( " List 1 Separated by space: ").split()
l2 = input( " List 2 Separated by space: ").split()

s1 , s2 = set(l1) , set(l2)

print(" Common items of lists : ",list(s1.intersection(s2)))   #intersection of listsa
