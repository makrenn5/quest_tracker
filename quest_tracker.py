
quest_list = []

def quest_log():
    print("====================")
    print("     QUEST LOG      ")
    print("====================")
    print("                    ")
    print("Hello adventurer! Ready for a quest?")
    print("                    ")
    print("1. View quests")
    print("2. Add quest")
    print("3. Complete quest")
    print("4. Delete quest")
    print("5. Quit")
    print("                    ")

def view_quest():
    print("Your Active Quests:")
    print("                   ")
    print(len(quest_list))
    quest_count = 1

    for quest in quest_list:
        print(f"{quest_count}.  " + f"{quest['title']}")
        print(f"{quest['description']}")
        quest_count += 1


def add_quest():
    new_quest = {}
    quest_name = input("What is the name of the quest? ")
    quest_description = input("Please describe the quest. ")
    new_quest["title"] = quest_name
    new_quest["description"] = quest_description
    quest_list.append(new_quest)
    print(new_quest)
    print("Quest added successfully!")
    
# def complete_quest():

# def delete_quest():
    
def main():
    main_menu_options = {
        1: "View quests", 
        2: "Add quests",
        3: "Complete quest",
        4: "Delete quest",
        5: "Quit"
        }
    
    while True:
        quest_log()
            
        while True:
            user_choice = input("Choose an option: ")

            try:
                number = int(user_choice)

                if number in main_menu_options:
                    break
                else:
                    print("Please choose from one of the available options.")

            except ValueError:
                print("That's not a valid option. Please try again. \n")

        print(f"You have selected: {main_menu_options[number]}")

        if number == 1:
            view_quest()

        elif number == 2:
            add_quest()

        elif number == 3:
            complete_quest()

        elif number == 4:
            delete_quest()

        elif number == 5:
            print("So long adventurer!")
            break


main()


    
    


