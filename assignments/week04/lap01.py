"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""
"""
# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()
"""
def personal_info_manager():
    # Create initial person tuple
    person = ("Porawee",19, "chonburi", "Thai")  # name, age, city, country
    hobbies = []

    while True:
        choice = input("what do you to do?(1:dispay,2.add hobby,3.remove hobby,4.edit age,5.Exit)")

        if choice == "1":
            print("name",person[0])
            print("Age",person[1])
            print("City",person[2])
            print("Country",person[3])
            print("Hobbies :",hobbies)

        elif choice == "2":
            hobby = input("what is your new hobbies :")
            hobbies.append(hobby)

        elif choice == "3":
            hobbies.pop()

        elif choice == "4":
            person_list = list(person)
            age = input("How old are you? :")
            person_list[1] = age
            person = tuple(perrson_list)

        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()
