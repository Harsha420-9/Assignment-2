dict1 = {}
for i in range(ord(input("starting alphabet: ")), ord(input("Ending alphabet: "))+1):
    dict1[chr(i)] = i

print('Ascii values of the alphabets is : ',dict1)