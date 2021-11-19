
class Contacts:
    def __init__(self, name, address, phone_num, birthday):
        self.Name = name
        self.Address = address
        self.Phone_num = phone_num
        self.Birthday = birthday

    # function to add to file all the details of an element
    def add_to_file(self):
        # print("here2") to check if the method is being used
        # open the file using 'a'(=append)
        with open("Contacts.txt", 'a') as MyFile:
            # added the \n at the beginning to make sure the line is written in a new line
            LineToBeWritten = "\n" + self.Name + "," + self.Address + "," + self.Phone_num + "," + self.Birthday
            MyFile.write(LineToBeWritten)


def search_for_contact(choice2):
    if choice2 == 1:
        name = input("Name?").title()
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                NewLine = line.rstrip("\n").split(",")
                if NewLine[0] == name:
                    print("This is the contact with the name", name + ":")
                    print(NewLine)
                line = MyFile.readline()

    elif choice2 == 2:
        PhoneNum = input("Telephone?").replace(" ", "")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                NewLine = line.rstrip("\n").split(",")
                if NewLine[2] == PhoneNum:
                    print("This is the contact with the phone number", PhoneNum + ":")
                    print(NewLine)
                line = MyFile.readline()

    elif choice2 == 4:
        birthday = input("Enter the birthday in the format dd/mm/yyyy?")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            while line != "":
                NewLine = line.rstrip("\n").split(",")
                if NewLine[3] == birthday:
                    print("This is the contact with the birthday", birthday + ":")
                    print(NewLine)
                line = MyFile.readline()

    elif choice2 == 3:
        address = input("Address?")
        with open("Contacts.txt", 'r') as MyFile:
            line = MyFile.readline()
            # print("here")
            while line != "":
                NewLine = line.rstrip("\n").split(",")
                # print("here2")
                if NewLine[1] == address:
                    # print("here3")
                    print("This is the contact with the address", address + ":")
                    print(NewLine)
                line = MyFile.readline()


def retrieve_all_contacts():
    with open("Contacts.txt", 'r') as MyFile:
        line = MyFile.readline()
        print("This are all the contacts and their details:\n")
        while line != "":
            print(line.rstrip("\n"))
            line = MyFile.readline()

def change_detail_contact():
    name = input("What is the name of the contact you want some details to be changed?").title()
    with open("Contacts.txt", 'r') as MyFile:
        line = MyFile.readline()
        count = 0
        while line != "":
            NewLine = line.rstrip("\n").split(",")
            if NewLine[0] == name:
                print("These are the details of the contact\n", NewLine)
                LineNumber = count
                LineToBeChanged = NewLine
            count = count + 1
            line = MyFile.readline()
    MyFile = open("Contacts.txt", 'r')
    lines = MyFile.readlines()
    MyFile.close()
    choice4 = int(input("""What do you want to change?
    1) Name
    2) Address
    3) Birthday
    4) Telephone"""))
    if choice4 == 1:
        NewName = input("Enter the new name:").title()
        lines[LineNumber] = NewName + "," + LineToBeChanged[1] + "," + LineToBeChanged[2] + "," + LineToBeChanged[3] + "\n"
    elif choice4 == 2:
        NewAddress = input("Enter the new address")
        lines[LineNumber] = LineToBeChanged[0] + "," + NewAddress + "," + LineToBeChanged[2] + "," + LineToBeChanged[3] + "\n"
    elif choice4 == 3:
        NewBirthday = input("Enter the new birthday")
        lines[LineNumber] = LineToBeChanged[0] + "," + LineToBeChanged[1] + "," + LineToBeChanged[2] + "," + NewBirthday + "\n"
    elif choice4 == 4:
        NewTelephone = input("Enter the new telephone number").replace(" ", "")
        lines[LineNumber] = LineToBeChanged[0] + "," + LineToBeChanged[1] + "," + NewTelephone + "," + LineToBeChanged[3] + "\n"
    else:
        print("Need to choose only from the 4 options available")
        change_detail_contact()
    MyFile = open("Contacts.txt", 'w')
    MyFile.writelines(lines)
    MyFile.close


def delete_contact():  # maybe proof it a little better
    with open("Contacts.txt", 'r') as MyFile:
        lines = MyFile.readlines()
    name = input("What is the name of the contact you want to delete").title()
    length = len(name)
    with open("Contacts.txt", 'w') as MyFile:
        for line in lines:
            # writes every line that is not the line with the chosen name in the file
            if line[:length] != name:
                MyFile.write(line)


def create_new_contact():
    CreateName = input("Enter the name of the contact").title()

    CreateAddress = input("Enter the address").title()

    CreatePhone = input("Enter the phone number of the contact").replace(" ", "")

    CreateBday = input("Enter the birthday in the format dd/mm/yyyy")
    # Make the new_item an element of the class
    NewItem = Contacts(CreateName, CreateAddress, CreatePhone, CreateBday)
    #print("Here")
    Contacts.add_to_file(NewItem)
