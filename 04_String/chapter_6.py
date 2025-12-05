chai_order = dict(type="Masala Chai", size = "Large", sugar=2)

print(f"chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"


print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")


print(f"Is sugar in order? {'sugar' in chai_order}")

chai_order = dict(type="Ginger Chai", size = "Medium", sugar=1)

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")


last_item = chai_order.popitem()
print(f"Removed last item : {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"updated chai recipe: {chai_recipe}")

ccustomer_note = chai_order.get("note", "No Note")
print(f"Chai size is: {ccustomer_note}")