flavours = ["Gingrt", "Oust od stock", "Lemom"
"Discintenued"]

for flavours in flavours:
    if flavours == "Out od stock":
        continue 
    if flavours == "Discontinued":
        break
    
    print("Discountoined item found")

print(f"Out side of loop")