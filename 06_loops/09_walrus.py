# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
    
else:
    print(f"Size is unavialble = {requested_size}")
    
flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavours)

while (flavours := input("choose your flavor: ")) not in flavours:
    print(f"Sorry, {flavours} is not availbale")
    
print(f"You choose {flavours} chai") 