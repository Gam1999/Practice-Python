InputText = input("Enter text: ")
InputWord = input("Enter filter word: ")
String = InputText.replace(InputWord, "*" * len(InputWord))
print('Text after filter is "' +String +'"') 