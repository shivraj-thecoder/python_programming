## Data Types and Variables
### Variable Declaration:
### 1 Create variables of different data types (integer, float, string, boolean) and assign values to them.
### 2 Print the values of these variables.
try:
    Integer_value=int(input('Enter some Integer value:'))
    Float_value=float(input('Enter some Float value:'))
    String_value=str(input('Enter some String value:'))
    Bool_value=input('Enter some Boolean value (True | False | T | F): ').strip().lower()
    if Bool_value in ['true','t']:
        Bool_value = True
    elif Bool_value in ['false','f']:
        Bool_value = False
    else:
        raise ValueError('Invalid input for boolean value')
except Exception as E:
    print(f"Error:{E}.provide a correct form of value.")
else:
    print(f"Intger_value:{Integer_value}")
    print(f"Float_value:{Float_value}")
    print(f"String_value:{String_value}")
    print(f"Bool_value:{Bool_value}")


## Type Conversion:
### 1 Convert a string to an integer and vice versa.
### 2 Convert a float to an integer and vice versa.
### 3 Print the results.
try:
    value_a=input('Enter some value to convert in Integer').strip()
    covert_to_int=int(value_a)
    print(f"Successfully converted to integer:{covert_to_int}")
except Exception as E:
    print(f"Error:{value_a} is not valid integer.Please provide valid integer value")

value_b = input('Enter some value to convert in String').strip()
convert_to_String = str(value_b)
print(f'Successfully converted into to the string:{convert_to_String}')
try:
    value_c =  input('Enter some value to convert in Float').strip()
    convert_to_float=float(value_c)
    print(f'Successfully converted into flaot: {convert_to_float}')
except Exception as E:
    print(f'Error:{value_c} is not a valid to convert to float. please provide valid value.')
try:
    value_d = input('Enter some value to convert in bool ').strip().lower()
    if value_d in ['true','1'] or (value_d.isdigit() and int(value_d)>1):
        value_d = True
        print(f'Converted to boolean:{value_d}')
    elif value_d in ['false','0']:
        value_d = False
        print(f'Converted to boolean:{value_d}')
    else:
        raise ValueError(f"{value_d}is not valid boolean input")
except Exception as E:
    print(f"Error:{E} Please provide valid input to convert to bool.")



## Arithmetic Operations:
### 1 Perform addition, subtraction, multiplication, division, and modulus operations on integers and floats.
### 2 Print the results.

## Integer Arithmetic Operation 
H_int = 1000
I_int = 15
print('Integer arithmetic Operations:')
print(f"Addition: {H_int} + {I_int} = {H_int + I_int}")
print(f'Substraction: {H_int} - {I_int} = {H_int - I_int}')
print(f'Multiplication: {H_int} * {I_int} = {H_int * I_int}')
print(f'Division: {H_int} / {I_int} = {H_int / I_int}')
print(f'Modulus: {H_int} % {I_int} = {H_int % I_int}')

## Float Arithmetic Operation 
H_int = 1001.1001
I_int = 101.101
print('Float arithmetic Operations:')
print(f"Addition: {H_int} + {I_int} = {H_int + I_int}")
print(f'Substraction: {H_int} - {I_int} = {H_int - I_int}')
print(f'Multiplication: {H_int} * {I_int} = {H_int * I_int}')
print(f'Division: {H_int} / {I_int} = {H_int / I_int}')
print(f'Modulus: {H_int} % {I_int} = {H_int % I_int}')



## Concatenate two strings.
### 1 Find the length of a string.
### 2 Extract a substring from a string.
### 3 Replace a substring within a string.

Str_1 = 'Hello my name is '
Str_2 = 'Shivraj'

## Concatenation of two string
Final_str = Str_1 + Str_2
print(f"Concatenation of two string: {Final_str}")

## Extract a substring from a string.
Substring = Final_str[0:10]
print(f"Extract a substring from a string:{Substring}")

## Find the length of a string.
Length_of_string = len(Final_str)
print(f"length of a string:{Length_of_string}")

## Replace a substring within a string.
Replace = Final_str.replace('Shivraj','Aarav')
print(f"New string after replace operation:{Replace}")



## Lists:
### 1 Create a list of integers, floats, strings, and booleans.
### 2 Access elements in the list using indexing.
### 3 Modify elements in the list.
### 4 Append, insert, and remove elements from the list.
### 5 Print the results.

### 1.Create a list of integers, floats, strings, and booleans.
list = [1,10.01,'SP',True,False]
print(list)

### 2 Access elements in the list using indexing.
access = list[:5:2]
print(access)

### 3. Modify elements in the list.
list[0] = 200
print('List after modification:',list)

#### 4. Append, insert, and remove elements from the list.
## Original string
print(list)

## apped operation
list.append(1001)
print(list)

## Insert element
list.insert(2,'Shivraj')
print(list)

## Remove element
list.remove(False)
print(list)


## Tuples:
### 1 Create a tuple of integers, floats, strings, and booleans.
### 2 Access elements in the tuple using indexing.
### 3 Try to modify elements in the tuple (should raise an error).
### 4 Print the results.



### 1 Create a tuple of integers, floats, strings, and booleans.
tuple = (100,1837.87,'Shivraj',True,False)
print(tuple)

### 2. Access elements in the tuple using indexing.
first_element = tuple[0]
print(first_element)


### 3. Try to modify elements in the tuple (should raise an error).
#### Tuple is immutable
My_Tuple=(10,'Shivraj',4555,'Ajinkya')
print(My_Tuple)
try:
    My_Tuple[0]=100
except TypeError as E :
    print(f'Error:{E} Tuple is Immutable we can not modify the tuple')


## Dictionaries:
### 1 Create a dictionary with keys and values of different data types.
### 2 Access values in the dictionary using keys.
### 3 Modify values in the dictionary.
### 4 Add and remove key-value pairs.
### 5 Print the results.



### 1 Create a dictionary with keys and values of different data types.
my_dic={'Name':"Shivraj","Age":25,"Marks":100.01,"Student":True}
print(my_dic)

### 2. Access values in the dictionary using keys.
name = my_dic['Name']
print('Name of student:',name)

### 3. Modify values in the dictionary.
my_dic['Age']=26
print(my_dic)

### 4. Add and remove key-value pairs.
### 1. adding values
my_dic['Course'] = 'Data Science'
print(my_dic)

### 2. remove key value pair
del my_dic['Student']
print(my_dic)


## Control Flow
### Conditional Statements (if-else):
### 1 Write a program to check if a number is positive, negative, or zero.
### 2 Write a program to check if a year is a leap year.

### 1. Write a program to check if a number is positive, negative, or zero.
number = int(input('Enter number only 0,1,-1 :'))
if number > 0:
    print('The number positive')
elif number < 0:
    print('The number is negative')
else:
    print('The number is zero')



### 2. Write a program to check if a year is a leap year.
year = int(input('Enter a year:'))
if (year%400==0):
    print(year,'is a leap year')
else:
    print(year,"is not a leap year")


## Functions
#### Function Definition:
#### 1 Define a function to calculate the area of a circle.
#### 2 Define a function to check if a number is prime.



### 1. Define a function to calculate the area of a circle.
def area_of_circle(radius):
    pi = 3.14
    area =pi*(radius**2)
    return area
print(area_of_circle(5))


### 2. Define a function to check if a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True 
print(is_prime(13))


## Function Calling:
## 1 Call the functions you defined and print the results.
print(area_of_circle(5))
print(is_prime(13))


## Function Arguments:
### 1 Define a function that takes multiple arguments.
### 2 Call the function with different arguments.
def total_cost(*prices):
    total = sum(prices)
    return total
item_1 = total_cost(10,20,30,40)
print("Total_item_1: ",item_1)
item_2 = total_cost(102240,2840,3540,4540)
print("Total_item_2: ",item_2)
