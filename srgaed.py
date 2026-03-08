def get_discounted_prices(prices: list):
    discounted_prices = []

    for price in prices:
        if price > 100:
            discounted_prices.append(price * 0.8)
    
    return discounted_prices

original_prices = [50, 120, 80, 200, 300]
result = get_discounted_prices(original_prices)
print(result)