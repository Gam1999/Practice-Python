InputChar = input("Enter 5 characters: ").strip().lower()
ans = ""
for i in InputChar:
    ans += chr(219 -ord(i))
print("Encryption is",ans)