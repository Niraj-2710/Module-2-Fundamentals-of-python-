# Write python program that swap two number with temp variable and without temp variable.


x = int(input("Value of x :"))
y = int(input("Value of y :"))
x, y = y, x
print("The Value of x After Swapping :",x)
print("The Value Of y After Swapping :",y)
print("*"*20)
x = int(input("Value Of X :"))
y = int(input("Value Of Y :"))
temp = x
x = y
y = temp
print("The Value of x After Swapping :",x)
print("The Value Of y After Swapping :",y)