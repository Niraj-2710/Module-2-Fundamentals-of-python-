# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.


num = int(input("Enter Any Number :"))
if (num % 2) == 0:
    print("{0} Is Even Number".format(num))
else:
    print("{0} Is Odd Number".format(num))