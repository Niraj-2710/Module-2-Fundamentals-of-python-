S = input("Enter A String :")

if len(S) % 4 == 0:
    S = S[::-1]
print(S)