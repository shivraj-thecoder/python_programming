def swap_temp(value_one,value_two):
    temp=value_one
    value_one=value_two
    value_two=temp
    return value_one,value_two
    

X=input("enter value of X :")
Y=input("enter value of Y :")
X, Y=swap_temp(X,Y)
print('value of X after swapping:', X)
print('value of Y after swapping:', Y)