tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 90 for tea, price in tea_prices_inr.items() }

print(tea_prices_usd)
