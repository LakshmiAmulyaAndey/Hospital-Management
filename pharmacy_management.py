phastock = {"saradon": 10}
pha = {}
preq = []

def pregister():
    print("--- PHARMACY REGISTRATION PAGE ---")
    pha_name = input("Enter your pharmacy name: ")
    email = input("Enter your email: ")
    password = input("Enter password: ")

    if pha_name in pha:
        print("Pharmacy already exists.")
        return
    pha[pha_name] = {"email": email, "password": password}
    print("Account Created Successfully!")

def plogin():
    print("--- PHARMACY LOGIN PAGE ---")
    pha_name = input("Enter your pharmacy name: ")
    password = input("Enter your password: ")

    if pha_name in pha and pha[pha_name]['password'] == password:
        print("Login successful!")
        while True:
            print("\n1. Stock details")
            print("2. Add Stock")
            print("3. Request Medicine from Company")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                print("Pharmacy Stocks:", phastock)
            elif choice == 2:
                mname = input("Enter medicine name: ")
                mno = int(input("Enter quantity: "))
                phastock[mname] = phastock.get(mname, 0) + mno
                print("Stock added successfully!")
            elif choice == 3:
                med_name = input("Enter medicine name: ")
                quantity = int(input("Enter quantity: "))
                preq.append({"pharmacy": pha_name, "medicine": med_name, "quantity": quantity})
                print("Request sent successfully!")
            elif choice == 4:
                print("Exiting pharmacy login.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid login details.")

def pharmacy():
    print("--- WELCOME TO PHARMACY MANAGEMENT ---")
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            pregister()
        elif choice == 2:
            plogin()
        elif choice == 3:
            print("Exiting Pharmacy Management...")
            break
        else:
            print("Invalid choice. Please try again.")
