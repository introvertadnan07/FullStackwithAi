seat_type = input("Enter seat type (sleeper/AC/General/Luxuary) = ").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No Ac, beds available")
    case "ac":
        print("Ac - Air conditioned, comfy ride")
        
    case "general":
        print("General = Cheapest option, noreservation")
        
    case "luxuray":
        print("Luxury - Premium seats with meals")
        
    case _:
        print("Invalid seat type")
    