string = input("Enter A string :")

poor_index = string.find("poor")
not_index = string.find("not")

if poor_index != -1 and not_index != -1 and not_index < poor_index:
    string = string[:not_index]  + "Good" + string[poor_index + 4:]

print(string)





