users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F24"},
    {"id": 3, "total": 190, "coupon": "R15"}
]

discounts = {
    "P20": (0.2, 0),
    "F24": (0.5, 0),
    "R15": (0.8, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    user_discount = user["total"] * percent + fixed

    print(
        f'User ID: {user["id"]}\n'
        f'Paid: {user["total"]}\n'
        f'Discount for next visit: {user_discount}\n'
    )
