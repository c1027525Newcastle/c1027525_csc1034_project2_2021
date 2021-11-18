class Contacts:
    def __init__(self, name, address, phone_num, birthday):
        self.Name = name
        self.Address = address
        self.Phone_num = phone_num
        self.Birthday = birthday

    def set_name(self, name): #still need to work on this
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")

#def create_new_contact():

def search_for_contact(choice2):
    #Still need to change the method where it calls the main() as it's stopping at the first found element/no duplicates are found
    if choice2 == 1:
        name = input("Name?")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                newline = line.split(",")
                if newline[0] == name:
                    print("This is the contact with the name", name +":")
                    print(newline)
                    main()
                line = MyFile.readline()

    elif choice2 == 2:
        phone_num = input("Telephone?")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                newline = line.split(",")
                if newline[2] == phone_num:
                    print("This is the contact with the phone number", phone_num +":")
                    print(newline)
                    main()
                line = MyFile.readline()

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
            search_for_contact(choice2)

        elif choice == 3:
            print("Your choice was 3")

        else:
            print("You can oly choose from the 3 options")
            main()

    except:
        print("Please choose one by inserting an integer")
        main()

main()