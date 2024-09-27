A = input("Enter String :")
str = input("Enter String To Insert :")

index = len(A)
result = A[:index] + str + A[index:]

print("The Resulting String is :",result)