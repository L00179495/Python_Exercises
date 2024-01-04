#Calculate most expensive phone from the list
def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive phone
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    # Iterate, unpacking the tuple
    for description, price in price_list:
        # If this is the maximum price, record that in our variables
        if price > max_price:
            max_price = price
            max_price_item = description
        # If it is not the maximum price, do nothing
        else:
            pass
    # Return the maximum prices item and its price
    return max_price_item, max_price

# Provide the price in Euros
price_list = [("Apple iphone", 2000), ("Samsung", 1000), ("Lenovo", 750), ("One plus", 650)]
# Call the function and unpack its return values
product, price  = most_expensive(price_list)
print('Most expensive phone is :',product, ',Price is',price ,'Euros')