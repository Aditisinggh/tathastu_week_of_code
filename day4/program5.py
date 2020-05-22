import collections as c

array = input(' Enter comma separated array of candidates : ').split()
dic = dict(c.Counter(array))

dic1 = { v:k for k ,v in dic.items()}
m = max(dic1)
print(' Maximum Votes({}) Candidate : {} '.format( m , dic1[m]))
