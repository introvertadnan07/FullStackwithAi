masla_spices = ("cardamom", "cloves", "cinnamon")


(spice1, spice2, spice3) = masla_spices

print(f"Main masla spices : {spice1}, {spice2},{spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G : {ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G : {ginger_ratio} and C: {cadramom_ratio}")

# membership

print(f"Is ginger in masala spices ? {'ginger' in masla_spices}")
print(f"Is ginger in masala spices ? {'cinnamon' in masla_spices}")