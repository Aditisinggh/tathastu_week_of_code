def maximal(l) :
    l = list(map(int , l))
    s = sum(l[::2])
    return(s)

house_value = input( ' Enter comma separated house value of each house : ').split(',')

print(' Maximal value stolen by the thief : ' , maximal(house_value))
