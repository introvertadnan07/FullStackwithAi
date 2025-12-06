device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperture alrt!")
    else:
        print("Temperature is normal")
        
else:
    print("Device is ofline")