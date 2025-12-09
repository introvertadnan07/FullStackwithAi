daliy_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daliy_sales if sale > 5)

print(total_cups)