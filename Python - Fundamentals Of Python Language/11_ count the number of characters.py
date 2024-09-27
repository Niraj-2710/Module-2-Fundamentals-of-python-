
freq = {}

S = (input("Enter A String : "))

index = 0
for char in S:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
    index += 1
    
for char,freq in freq.items():
    print(char," : ",freq)