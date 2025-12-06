names = ["Anum", "Adnan", "Orhan", "Madeeha"]
bills = [50, 100, 55, 67]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")