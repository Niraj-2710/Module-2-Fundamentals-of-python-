# program to get the Factorial number of given number. 


n = int(input("Enter Number :"))
F = 1
for i in range(n,0,-1):
    F=F*i
print(F,"Is Factorial Number")