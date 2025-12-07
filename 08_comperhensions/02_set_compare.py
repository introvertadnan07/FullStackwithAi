favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elcaichi Chai"
]

unique_chai = { chai for chai in favourite_chais if len(chai) < 8} 
print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "spicy Chai": ["ginger", "Black", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)