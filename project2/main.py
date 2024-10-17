import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name,"age": age,"email": email,}
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"] )
        #The reason I say i + 1 is cause I dont want to start counting at 0 KINDA OFF!

def delete_contact(people):
    display_people(people)

    while True:
    #I need to keep asking for an input till is valide that is why I put the while loop.
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalide input.")
    people.pop(number - 1)

def search(people):
    search_name = input("Search for a name: ").lower()
    result = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
#Here I am checking if the string that is passed in the input value can be found inside name: which I assigned to be the key pair value inside my
#person dictionary
#So if there is a match take this item and add it to my result empty list
            result.append(person)
    display_people(result)

print("Welcome to the Contact Managment System.")
print()

with open("contacts.json","r") as f:
    people = json.load(f)["contacts"]


while True:
    print()
    print("Contact list size: ", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' and 'Q' to quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == 'delete':
        delete_contact(people)
        print("Contact removed.")
    elif command == "search":
        search(people)
    elif command == "q":
        print("Bye bye")
        break
    else:
        print("Invalid command.")



with open("contacts.json","w") as f:
    json.dump({"contacts": people},f)