class Contacts:
    def __init__(self, name, address, phone_num, birthday):
        self.Name = name
        self.Address = address
        self.Phone_num = phone_num
        self.Birthday = birthday

#def create_new_contact():

def main():
    try:
        choice = int(input("""What do you want to do:
    1) Create a new contact
    2) Search for a contact
    3) Retrieve all contacts and their details
    Answer:"""))
        print(choice)

        if choice == 1:
            print("Your choice was one")

        elif choice == 2:
            choice2 = int(input("""How do you want to search for the contact?
    By looking for the:
    1)Name
    2)Phone number
    3)Address
    4)Birthday
    Answer"""))
            print(choice2)

        elif choice == 3:
            print("Your choice was 3")

        else:
            print("You can oly choose from the 3 options")
            main()

    except:
        print("Please choose one by inserting an integer")
        main()

main()