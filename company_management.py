from hospital_management import  hreq
from pharmacy_management import preq
company_names = {}
comstock = {"p650": 8}


def register():
    print("--- COMPANY REGISTRATION PAGE ---")
    company_name = input("Enter your company name: ").strip()
    while not company_name:
        print("Invalid Name! Please enter a valid name")
        company_name = input("Enter your company name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    username = input("Enter your username: ").strip()
    
    if username in company_names:
        print("Username already exists. Please choose a different username.")
        return
    company_names[username] = {"company_name": company_name, "email": email, "password": password}
    print("Account Created Successfully!")

def login():
    print("--- COMPANY LOGIN PAGE ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in company_names and company_names[username]['password'] == password:
        print("Login successful!")
        while True:
            print("\n1. Stock details")
            print("2. Add Stock")
            print("3. View Hospital Requests")
            print("4. View Pharmacy Requests")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                print("Company Stocks:", comstock)
            elif choice == 2:
                mname = input("Enter medicine name: ")
                mno = int(input("Enter quantity: "))
                comstock[mname] = comstock.get(mname, 0) + mno
                print("Stock added successfully!")
            elif choice == 3:
                print("Hospital Requests:", hreq)
            elif choice == 4:
                print("Pharmacy Requests:", preq)
            elif choice == 5:
                print("Exiting company login.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password.")

def company():
    print("--- WELCOME TO COMPANY MANAGEMENT ---")
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
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Exiting Company Management...")
            break
        else:
            print("Invalid choice. Please try again.")
