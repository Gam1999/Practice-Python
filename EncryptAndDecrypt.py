import string
ROT13Encrypt = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
ROT13Decrypt = str.maketrans(
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

print("Select 2 options")
print(" - 1 encrypt with ROT 13")
print(" - 2 decrypt with ROT 13\n")
InputOption = int(input("Choose option: "))
InputText = input("Enter text: ")
TextEncrypt = ""
TextDecrypt = ""

if InputOption == 1:
    TextEncrypt = str(InputText).translate(ROT13Encrypt)
    print('Ciphertext is "'+TextEncrypt+'"')
else:
    TextDecrypt = str(InputText).translate(ROT13Decrypt)
    print('Plaintext is "'+TextDecrypt+'"')