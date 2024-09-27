T = input("Enter A String : ")

if len(T) < 3:
    print(T)
elif T[-3:] == "ing":
    print(T + "ly")
else: 
    print(T + "ing")
