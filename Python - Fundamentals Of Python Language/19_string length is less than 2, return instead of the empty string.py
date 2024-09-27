s = input("Enter String :")

if len(s) <2:
    s = "instead"
else:
    s = s[:2] + s[-2:]
print(s) 
