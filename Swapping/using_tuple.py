def swap_tuple(value_one,value_two):
    value_one,value_two=value_two,value_one
    return value_one,value_two

X=input("enter value of X :")
Y=input("enter value of Y :")
X, Y=swap_tuple(X,Y)
print('value of X after swapping:', X)
print('value of Y after swapping:', Y)