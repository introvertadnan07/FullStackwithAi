staff = [("Amit", 16), ("Zara", 21), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to mange the staff")
        break
    
else:
    print(f"No one is eligible to mange the staff")