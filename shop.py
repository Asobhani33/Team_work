def open_shop():
    print("\nWelcome to the shop!")
    print("1. Buy a sword")
    print("2. Buy an apple")
    print("3. Buy a diamond")
    print("4. Buy a dog")
    print("5. I don't want to buy anything")

    choice = input("Choose and write a number(1-4): ")
    if choice == "1":
        print("You bought a sword!")

    elif choice == "2":
        print("You bought an apple!")
    
    elif choice == "3":
        print("You bought a diamond!")
    
    elif choice == "4":
        print("You bought a dog!")

    elif choice == "5":
        print("You don't buy anything!")
  
    else: 
        print ("Wrong choice!")