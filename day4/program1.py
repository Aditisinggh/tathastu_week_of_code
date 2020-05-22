tup = input(' Enter tuple elements (space separated) : ').split()
tup = tuple(tup)
n   = input(' Enter element to be counter : ')
print( ' Number of {} in {} : {} '.format( n, tup , tup.count(n)))

