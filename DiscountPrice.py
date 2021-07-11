lists = {"food" : 0.03, "medicine" : 0.01, "shoes" : 0.20}

def cal(InputType , price):
    DiscountPrice = float(price)
    if lists.get(InputType) != None:
        DiscountPrice = float(price) *( 1 - lists[InputType])
    return DiscountPrice

InputType = input("Enter product type: ")
InputPrice = input("Enter price: ")

product_discount = cal(InputType,InputPrice)
print("Price after discount is {:.2f}".format(product_discount))

