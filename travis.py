known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi!My name is Travis" )
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print( "Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        
        if remove == "y":
            known_users.remove(name) 

    else:
        print("Hmmm i dont think i have met you yet {}".format(name))
        add_me = input("would you like to be added toe the system (y/n)?: ").strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("no worries se you around!")

            
