company_names = {}
hspstock = {"dolo": 5}
comstock = {"p650": 8}
phastock = {"saradon": 10}
hsp = {}
pha = {}
hreq = []
preq = []

def register():
    print("--- REGISTRATION PAGE ---")
    company_name = input("Enter your company name: ").strip()
    while not company_name:
        print("Invalid Name! Please enter a valid name")
        company_name=input("Enter your company name:").strip()
    email = input("Enter your email: ").strip()
    while not email:
        print("Invalid Name! Please enter a valid name")
        email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    while not password:
        print("Invalid Name! Please enter a valid password")
        password = input("Enter your password: ").strip() 
    username = input("Enter your name: ").strip()
    while not username:
        print("Invalid Name! Please enter a valid name")
        username = input("Enter your  UserName: ").strip()
    
    if username in company_names:
        print("Username already exists. Please choose a different username.")
        return
    company_names[username] = {"company_name": company_name, "email": email, "password": password}
    print("Account Created Successfully")
    print(company_names)

def login():
    print("--- LOGIN PAGE ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in company_names and company_names[username]['password'] == password:
        print("Login successful!")
        while True:
            print("1. Stock details")
            print("2. Add Stock")
            print("3. Request from hospital management")
            print("4. Request from pharmacy management")
            print("5. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if choice == 1:
                print("Stocks are:", comstock)
            elif choice == 2:
                mname = input("Enter medicine name: ")
                mno = int(input("Enter quantity: "))
                comstock[mname] = comstock.get(mname, 0) + mno
                print("Stock added successfully!")
            elif choice == 3:
                print("Requests from hospital management:", hreq)
            elif choice == 4:
                print("Requests from pharmacy management:", preq)
            elif choice == 5:
                print("Exiting Company login.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password.")

def company():
    print("--- WELCOME TO COMPANY MANAGEMENT ---")
    while True:
        print("1. New to Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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

def hregister():
    print("--- REGISTRATION PAGE ---")
    hsp_name = input("Enter your hospital name: ")
    email = input("Enter your email: ")
    password=input("Enter password:")
    
    if hsp_name in hsp:
        print("Hospital name already exists.")
        return
    
    hsp[hsp_name] = {"email": email, "password": password}
    print("Account Created Successfully")

def hlogin():
    print("--- LOGIN PAGE ---")
    hsp_name = input("Enter your hospital name: ")
    password = input("Enter your password: ")

    if hsp_name in hsp and hsp[hsp_name]['password'] == password:
        print("Login successful!")
        while True:
            print("1. Stock details")
            print("2. Add Stock")
            print("3. Request medicine from company")
            print("4. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if choice == 1:
                print("Hospital stocks are:", hspstock)
            elif choice == 2:
                mname = input("Enter medicine name: ")
                mno = int(input("Enter quantity: "))
                hspstock[mname] = hspstock.get(mname, 0) + mno
                print("Stock added successfully!")
            elif choice == 3:
                med_name = input("Enter medicine name: ")
                quantity = int(input("Enter quantity: "))
                hreq.append({"hospital": hsp_name, "medicine": med_name, "quantity": quantity})
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
        print("1. New to Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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
def pregister():
    print("--- REGISTRATION PAGE ---")
    pha_name = input("Enter your pharmacy name: ")
    email = input("Enter your email: ")
    password = input("Enter your password:")
    
    if pha_name in pha:
        print("Pharmacy name already exists.")
        return
    pha[pha_name] = {"pha_name": pha_name, "password": password}
    print("Account Created Successfully")

def plogin():
    print("--- LOGIN PAGE ---")
    pha_name = input("Enter your Pharmacy name: ")
    password = input("Enter your password: ")

    if pha_name in pha and pha[pha_name]['password'] == password:
        print("Login successful!")
        while True:
            print("1. Stock details")
            print("2. Add Stock")
            print("3. Request medicine from company")
            print("4. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if choice == 1:
                print("Pharmacy stocks are:", phastock)
            elif choice == 2:
                mname = input("Enter medicine name: ")
                mno = int(input("Enter quantity: "))
                phastock[mname] = phastock.get(mname, 0) + mno
                print("Stock added successfully!")
            elif choice == 3:
                med_name = input("Enter medicine name: ")
                quantity = int(input("Enter quantity: "))
                preq.append({"hospital": pha_name, "medicine": med_name, "quantity": quantity})
            elif choice == 4:
                print("Exiting pharmacy login.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid login details.")
    
def pharmacy():
    print("---WELCOME TO PHARMACY MANAGEMENT---")
    while True:
        print("1.New to Register")
        print("2.Login")
        print("3.Exit")
        try:
            choice = int(input("Enter your choice:"))
        except ValueError :
            print("Invalid input. Please enter a valid number.")
            continue
        if choice ==1:
            pregister()
        elif choice == 2:
            plogin()
        elif choice == 3:
            print("Exiting Pharmacy Management...")
            break
        else:
            print("Invalid choice.Please try again.")
def dms():
    print("*** WELCOME TO DRUG MANAGEMENT SYSTEM ***")
    while True:
        print("1. Company Management")
        print("2. Hospital Management")
        print("3. Pharmacy Management")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            company()
        elif choice == 2:
            hospital()
        elif choice == 3:
            pharmacy()
        elif choice == 4:
             print("Exiting Drug Management System...")
             break        
        else:
            print("Invalid choice. Please try again.")
dms()
