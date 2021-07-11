InputNumber = input("Enter value in mm, cm, and m: ")
InputMmMCM = input("Enter unit to convert in mm, cm, m: ")

if InputNumber.find('m') != -1  and InputMmMCM == "cm":
    AnsInput = str(float(InputNumber.split("m")[0]) * 100.0) + "cm"
elif InputNumber.find('cm') != -1  and InputMmMCM == "m":
    AnsInput = str(float(InputNumber.split("cm")[0]) / 100.0) + "m"
elif InputNumber.find('mm') != -1  and InputMmMCM == "cm":
    AnsInput = str(float(InputNumber.split("mm")[0]) / 10.0) + "mm"
elif InputNumber.find('cm') != -1  and InputMmMCM == "mm":
    AnsInput = str(float(InputNumber.split("cm")[0]) * 10.0) + "mm"
elif InputNumber.find('m') != -1  and InputMmMCM == "mm":
    AnsInput = str(float(InputNumber.split("m")[0]) * 1000.0) + "mm"
elif InputNumber.find('mm') != -1  and InputMmMCM == "m":
    AnsInput = str(float(InputNumber.split("m")[0]) / 1000.0) + "m"
else:
    AnsInput = ans

print("Value after unit conversion is",AnsInput)