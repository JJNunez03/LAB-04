# Author: Jonathan Nunez
# Date: 9/22/24
# Purpose: Main program for Tuffy Titan contact management 

import contacts

def display_menu():
    print("\n*** TUFFY TITAN CONTACT MAIN MENU ***")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find contact")
    print("6. Exit the program")

def main():
    contact_dict = {}
    while True:
        display_menu()
        choice = input("Enter menu choice: ")

        if choice == "1":  
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.add_contact(contact_dict, id, first_name, last_name)
            if result == "error":
                print("Phone number already exists.")
            else:
                print(f"Added: {first_name} {last_name}.")

        elif choice == "2":  
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.modify_contact(contact_dict, id, first_name, last_name)
            if result == "error":
                print("Phone number does not exist.")
            else:
                print(f"Modified: {first_name} {last_name}.")

        elif choice == "3":  
            id = input("Enter phone number: ")
            result = contacts.delete_contact(contact_dict, id)
            if result == "error":
                print("Invalid phone number.")
            else:
                print(f"Deleted: {result[id][0]} {result[id][1]}.")

        elif choice == "4":  
            sorted_contacts = contacts.sort_contacts(contact_dict)
            print("\n==================== CONTACT LIST ====================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for id, names in sorted_contacts.items():
                print(f"{names[1]:<20} {names[0]:<20} {id}")
            print("=====================================================")

        elif choice == "5":  
            find = input("Enter search string: ")
            found_contacts = contacts.find_contact(contact_dict, find)
            print("\n================== FOUND CONTACT(S) ==================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for id, names in found_contacts.items():
                print(f"{names[1]:<20} {names[0]:<20} {id}")
            print("=====================================================")

        elif choice == "6":  
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
