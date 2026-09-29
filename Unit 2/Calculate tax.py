item_name = input ("Give me an item \n> ")
item_price = float(input ("What is the price of the item? \n> "))
tax_rate = 1.06875

def calculate_tax (item, price, rate):
    print (item + " costs " + str(price) + "before tax and " + str(round(item_price * rate, 2)) + " after tax.")

calculate_tax(item_name, item_price, tax_rate)