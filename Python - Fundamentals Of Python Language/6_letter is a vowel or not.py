# Write a Python program to test whether a passed letter is a vowel or not


l = input("Letter of the alphabet :")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a Vowel."%l)
elif  l == 'y':
    print("%s is sometimes a Vowel :"%l)
else:
    print("%s is a Consonant :"%l)