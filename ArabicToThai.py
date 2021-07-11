InputArabic = input("Enter only 5 Arabic number: ")
Arabic = '0123456789'
ThaiNumber = '๐๑๒๓๔๕๖๗๘๙'
t = ''
for i in InputArabic:
    List = Arabic.find(i)
    if(List != -1):
        t = t + ThaiNumber[List]
print("Thai number is "+str(t))