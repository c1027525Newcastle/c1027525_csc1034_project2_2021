class Contacts:
    def __init__(self, name, address, phone_num, birthday):
        self.Name = name
        self.Address = address
        self.Phone_num = phone_num
        self.Birthday = birthday

    # function to add to file all the details of an element
    def add_to_file(self):
        print("here2")
        # open the file ussing 'a'(=append)
        with open("Contacts.txt", 'a') as myfile:
            # added the \n at the beginning to make sure the line is written in a new line
            line_to_be_written = "\n" + self.Name + "," + self.Address + "," + self.Phone_num + "," + self.Birthday
            myfile.write(line_to_be_written)


def search_for_contact(choice2):
    if choice2 == 1:
        name = input("Name?").title()
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                newline = line.rstrip("\n").split(",")
                if newline[0] == name:
                    print("This is the contact with the name", name + ":")
                    print(newline)
                line = MyFile.readline()
        main()

    elif choice2 == 2:
        phone_num = input("Telephone?").replace(" ", "")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                newline = line.rstrip("\n").split(",")
                if newline[2] == phone_num:
                    print("This is the contact with the phone number", phone_num + ":")
                    print(newline)
                line = MyFile.readline()
        main()

    elif choice2 == 4:
        birthday = input("Enter the birthday in the format dd/mm/yyyy?")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                newline = line.rstrip("\n").split(",")
                if newline[3] == birthday:
                    print("This is the contact with the birthday", birthday + ":")
                    print(newline)
                line = MyFile.readline()
        main()

    elif choice2 == 3:
        address = input("Address?")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            # print("here")
            while line != "":
                newline = line.rstrip("\n").split(",")
                # print("here2")
                if newline[1] == address:
                    # print("here3")
                    print("This is the contact with the address", address + ":")
                    print(newline)
                line = MyFile.readline()
        main()


def retrieve_all_contacts():
    with open("Contacts.txt", 'r') as MyFile:
        line = MyFile.readline()
        print("This are all the contacts and their details:\n")
        while line != "":
            print(line.rstrip("\n"))
            line = MyFile.readline()


def change_detail_contact():
    name = input("What is the name of the contact you want some details to be changed?")
    with open("Contacts.txt", 'r') as MyFile:
        line = MyFile.readline()
        count = 0
        while line != "":
            newline = line.rstrip("\n").split(",")
            if newline[0] == name:
                print("These are the details of the contact\n", newline)
                line_number = count
                line_to_be_changed = newline
            count = count + 1
            line = MyFile.readline()
    myfile = open("Contacts.txt", 'r')
    lines = myfile.readlines()
    choice4 = int(input("""What do you want to change?
    1) Name
    2) Address
    3) Birthday
    4) Telephone"""))
    if choice4 == 1:
        new_name = input("Enter the new name:")
        lines[line_number] = new_name + "," + line_to_be_changed[1] + "," + line_to_be_changed[2] + "," + line_to_be_changed[3] + "\n"
    elif choice4 == 2:
        new_address = input("Enter the new address")
        lines[line_number] = line_to_be_changed[0] + "," + new_address + "," + line_to_be_changed[2] + "," + line_to_be_changed[3] + "\n"
    elif choice4 == 3:
        new_birthday = input("Enter the new birthday")
        lines[line_number] = line_to_be_changed[0] + "," + line_to_be_changed[1] + "," + line_to_be_changed[2] + "," + new_birthday + "\n"
    elif choice4 == 4:
        new_telephone = input("Enter the new telephone number")
        lines[line_number] = line_to_be_changed[0] + "," + line_to_be_changed[1] + "," + new_telephone + "," + line_to_be_changed[3] + "\n"
    else:
        print("Need to choose only from the 4 options available")
        change_detail_contact()
    myfile = open("Contacts.txt", 'w')
    myfile.writelines(lines)
    myfile.close
    main()


def delete_contact():  # maybe proof it a little better
    with open("Contacts.txt", 'r') as myfile:
        lines = myfile.readlines()
    name = input("What is the name of the contact you want to delete")
    length = len(name)
    with open("Contacts.txt", 'w') as myfile:
        for line in lines:
            if line[:length] != name:
                myfile.write(line)
    main()


def create_new_contact():
    create_name = input("Enter the name of the contact").title()

    create_address = input("Enter the address").title()

    create_phone = input("Enter the phone number of the contact").replace(" ", "")

    create_bday = input("Enter the birthday in the format dd/mm/yyyy")
    # Make the new_item an element of the class
    new_item = Contacts(create_name, create_address, create_phone, create_bday)
    print("Here")
    Contacts.add_to_file(new_item)
    return new_item


def main():
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
