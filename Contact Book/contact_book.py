contacts = {}

while True :

    print("\n =============CONTACT BOOK=============")
    print("1. Add Contacts.")
    print("2. View Contacts.")
    print("3. Search Contacts.")
    print("4. Delete Contacts.") 
    print("5. Exit.")

    choice = input("Enter your choice :")
    
    
    # Add Contacts
    if choice == '1':
        
        name = input("Enter Name :")
        phone = input("Enter Phone Number :")
        contacts[name] = phone

        print("Contact added successfully!")

    # View Contacts
    elif choice == '2':
        
        if len(contacts) == 0:
            print("No contacts found.")
        else :
            print("\n Your Contacts:")

            for name,phone in contacts.items():
                print("Name :",name)
                print("Phone Number :",phone)
                print() 

    # Search Contacts
    elif choice == '3':
        
        name = input("Enter name to search :")
        
        if name in contacts:
            print("Name :",name)
            print("Phone Number :",contacts[name])
        else :
            print("Contacts not found.")


    # Delete Contacts
    elif choice == '4' :
        
        name = input("Enter name to delete :")
        if name in contacts:
            del contacts[name]
            print("Contacts Deleted Successfully.")
        else :
            print("Contacts not found!")

    # Exit
    elif choice == '5':

        print("Thank you for using the contact book.")
        break

    else :
        print("Invalid choice. Please try again.")