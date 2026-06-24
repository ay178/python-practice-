"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""
def discount_price(price,discount_percent):
    discountprice=(discount_percent/100)*price
    final_amount=price-discountprice
    print(f" discount price = {discountprice}")
    print(f"final aoumnt to pay = {final_amount}")
price=int(input("enter the original price = "))
discount_percent=int(input("enter the percent of discount = "))
discount_price(price,discount_percent)
