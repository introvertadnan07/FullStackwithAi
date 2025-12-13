# file = open("order.txt", "w")
# file.write("Masala chai - 2 cups")

# try:
#     file.write("Masal chai - 2 cups")
    
# finally:
#     file.close()


with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")
    