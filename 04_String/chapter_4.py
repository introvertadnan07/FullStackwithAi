base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix : {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

raw_spice_data =bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")