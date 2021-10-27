# Create phonebook
"""
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for  is not found, print Not found instead.
"""
def display_menu():
    print("*" * 35)
    print("{:<1}{:^33}{:>1}".format("*", "Phonebook", "*"))
    print("*" * 35)
    print("\t1- Add Contact(s)")
    print("\t2- Print all Names and Numbers")
    print("\t3- Print all Contact Names")
    print("\t4- Search for contact by Name")
    print("\t5- Exit")
    print("*" * 35)


# option 1 - Add Contact(s)
def add_contact(name_in, number):
    phonebook.update({name_in: number})


# option 2 - Print Names and Numbers
def print_all_contacts():
    print("*" * 35)
    print("{0:<15}{1:<10}".format("Name", "Number"))
    print()
    for x, y in phonebook.items():
        print("{0:<15}{1:<10}".format(x, y))


# option 3 - print Names of contacts
def print_all_names():
    print("*" * 35)
    # using for loop
    for key in phonebook.keys():
        print(key)
    # # using lists
    # print(list(phonebook.keys()))
    # # using list comprehension
    # [print(key) for key in phonebook]


# option 4 - search for a contact
def find_contact(name_in):
    print("*" * 35)
    if name_in in phonebook.keys():
        print(f"{name_in} = {phonebook.get(name_in)}")
    else:
        print("ERROR\nNot Found!")


# main body of code
phonebook = {}
display_menu()
menu_option = int(input("Please Enter option:\t"))
while menu_option != 5:
    if menu_option == 1:
        print("*" * 35)
        opt = 'y'
        while opt == 'y':
            name = input("Enter contact's name:\t")
            num = input(f"Enter {name}'s number:\t")
            add_contact(name, num)
            opt = input("Do you wish to add another contact (y/n):\t").lower()
            while opt != 'y' and opt != 'n':
                print("Please enter a valid option: 'y' or 'n'!")
                opt = input("Do you wish to add another contact (y/n):\t").lower()
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    elif menu_option == 2:
        print_all_contacts()
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    elif menu_option == 3:
        print_all_names()
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    elif menu_option == 4:
        find_contact(input("Name to search for:\t"))
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    else:
        print("!ERROR!\n\tPlease enter a valid menu option\n\t1, 2, 3, 4, or 5")
        display_menu()
        menu_option = int(input("Please Enter option:\t"))