'''def calculate_discounted_price(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price

final_price = calculate_discounted_price(1000, 20)
print(final_price)

final_price1 = calculate_discounted_price(500, 10)
print(final_price1)

Final_price2 = calculate_discounted_price(200, 5)
print(Final_price2)'''


def get_discount(price):
    if price>= 500:  
        return 10 
    else :
        return 0

get_discount(1000)
print(get_discount(4455))
