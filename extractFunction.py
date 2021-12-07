def my_function(order: str):
    data = order.split('-')
    product = data[0]
    price = data[1]

    # format price
    price_as_number = int(price)
    formatted_price = f"{price_as_number:,}€"

    # print order with price
    stuff_in_string = f"product: {product}, price:{formatted_price}"
    print("-----------")
    print(stuff_in_string)
    print("-----------")


my_function('car-14000')
