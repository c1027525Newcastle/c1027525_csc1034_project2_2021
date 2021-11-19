from Main import *

def main():
    # this try and except are very broad as it will activate due to any reason in the whole program
    try:
        choice = int(input("""What do you want to do:
    1) Create a new contact
    2) Search for a contact
    3) Retrieve all contacts and their details
    4) Change the details of a contact
    5) Delete a contact
    6) Close program
    Answer:"""))

        if choice == 1:
            create_new_contact()

        elif choice == 2:
            choice2 = int(input("""How do you want to search for the contact?
    By looking for the:
    1)Name
    2)Phone number
    3)Address
    4)Birthday
    Answer"""))
            if choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4:
                search_for_contact(choice2)
            else:
                print("You can only choose from the 4 options")
                main()

        elif choice == 3:
            retrieve_all_contacts()

        elif choice == 4:
            change_detail_contact()

        elif choice == 5:
            delete_contact()

        elif choice == 6:
            print("Closing App")

        else:
            print("You can only choose from the 5 options")
            main()

    except:
        print("Please choose one by inserting an integer")
        main()


main()