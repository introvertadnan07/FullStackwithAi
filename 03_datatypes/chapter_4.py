is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions : {total_actions}")

milk_present = 0
print(f"Is there milk ? {bool(milk_present)}")


water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")