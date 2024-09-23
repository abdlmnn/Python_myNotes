num1 = input('Number one: ')
num2 = input('Number two: ')

result = num1 + num2
# when you add num1 and num2 
# the result is string
# result = 2 + 1

print(result)
# result = 21
# why because it is a string it read as a string 
# you can input any number and text it will print string


# To fix this you need to apply the casting before input(“ “). 
# You should add int( input(“number one: “) ).
num1 = int(input('Number one: '))
num2 = int(input('Number two: '))

# This is the propery way of casting 
# casting means converting a string into integers or vice versa

result = num1 + num2
# the num1 + num2 
# is now integers + integers
print(result)