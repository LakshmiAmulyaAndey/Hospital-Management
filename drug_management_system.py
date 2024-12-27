from company_management import company
from hospital_management import hospital
from pharmacy_management import pharmacy

def dms():
    print("*** WELCOME TO DRUG MANAGEMENT SYSTEM ***")
    while True:
        print("\n1. Company Management")
        print("2. Hospital Management")
        print("3. Pharmacy Management")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
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
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    dms()
