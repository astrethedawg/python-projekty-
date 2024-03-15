print("Hello, visitor!")
like_animals = input("Do you like animals? (yes/no)\n").lower().strip()

if like_animals == "yes":
    like_fish = input("Do you like fish? (yes/no)\n").lower().strip()
    
    if like_fish == "yes":
        like_sharks = input("Do you like sharks? (yes/no)\n").lower().strip()
        
        if like_sharks == "yes":
            print("Great! You are a fan of sharks.")
        elif like_sharks == "no":
            print("That's okay. Not everyone likes sharks.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    elif like_fish == "no":
        print("It seems you don't like fish.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

elif like_animals == "no":
    like_birds = input("Do you like birds? (yes/no)\n").lower().strip()
    
    if like_birds == "yes":
        print("Birds are wonderful creatures!")
    elif like_birds == "no":
        print("That's okay. Birds may not be your favorite.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
