hspstock = {"dolo": 5}
hsp = {}
hreq = []

def hregister():
    print("--- HOSPITAL REGISTRATION PAGE ---")
    hsp_name = input("Enter your hospital name: ")
    email = input("Enter your email: ")
    password = input("Enter password: ")

    if hsp_name in hsp:
        print("Hospital already exists.")
        return
    hsp[hsp_name] = {"email": email, "password": password}
    print("Account Created Successfully!")

def hlogin():
    print("--- HOSPITAL LOGIN PAGE ---")
    hsp_name = input("Enter your hospital name: ")
    password = input("Enter your password: ")

    if hsp_name in hsp and hsp[hsp_name]['password'] == password:
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
                print("Hospital Stocks:", hspstock)
            elif choice == 2:
                mname = input("Enter medicine name: ")
                mno = int(input("Enter quantity: "))
                hspstock[mname] = hspstock.get(mname, 0) + mno
                print("Stock added successfully!")
            elif choice == 3:
                med_name = input("Enter medicine name: ")
                quantity = int(input("Enter quantity: "))
                hreq.append({"hospital": hsp_name, "medicine": med_name, "quantity": quantity})
                print("Request sent successfully!")
            elif choice == 4:
                print("Exiting hospital login.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid login details.")

def hospital():
    print("--- WELCOME TO HOSPITAL MANAGEMENT ---")
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
            hregister()
        elif choice == 2:
            hlogin()
        elif choice == 3:
            print("Exiting Hospital Management...")
            break
        else:
            print("Invalid choice. Please try again.")
