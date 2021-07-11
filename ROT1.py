InputChar = input("Enter 3 characters: ").upper()
Ans = ""
if len(InputChar) == 3:
    for i in InputChar:
        if i == 'Z':
            Ans += 'A'
        else:
            Ans += chr(ord(i) + 1)
    print("Ciphertext is",Ans)
else:
    print("word length is mismatched")