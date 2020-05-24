def order(num_array) :
    num_array = list(map(int , num_array))

    odd_num = sorted( [ i for i in num_array if i%2 != 0] , reverse = True )
    even_num = sorted([ i for i in num_array if i%2 == 0] )
    num_array = odd_num + even_num

    return num_array

num_array =  input(' Enter comma separated lst of numbers : ').split(',')
print(' Modified array : ' , order(num_array))
