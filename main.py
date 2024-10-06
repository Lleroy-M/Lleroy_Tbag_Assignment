from room import Room
from character import Enemy
from character import character
from character import Friend

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining hall") 
key = item("Key", "A shiny gold key.")

dave = Enemy("Dave", "A smelly Zombie")
dave.set_conversation("hi im Dave i wont bite you!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

bob = character("Bob", "A friendly shopkeeper.")
ballroom.set_character(bob)

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shining gold plate")
dining_hall.set_description("A large room with ornate descriptions")

entrance_hall = Room("Entrance Hall", "A grand hall with a locked door to the north.")
entrance_hall.locked = True # Assuming 'locked' is an attribute of the Room class
dining_room = Room("Dining Room", "A large room with a long table.")

# ... placing the key ...
dining_room.set_item(key) 

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

current_room = kitchen

while True:
    print('\n')
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input('>')
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command in ["hug", "offer gift"] and isinstance(inhabitant, Friend):
        if command == "hug":
            inhabitant.hug()
    elif command == "talk":
        if inhabitant is not None:
                print("is talking!")
                inhabitant.talk()
        else:
                print("There's no one to talk to here.")  # Handle cases where there's no inhabitant
    elif command == "fight" and inhabitant is not None:
            weapon = input("What item do you want to fight with? ")
            if weapon == inhabitant.get_weakness():
                print("You defeated the enemy!")
                current_room.set_character(None)
            else:
                print("You failed to defeat the enemy.")
                print("You have died. Game Over!")
                exit()
    elif command in ["steal"] and isinstance(inhabitant, Enemy):
            # Check if the command is one of the new interactions and if an Enemy is present
            action = getattr(inhabitant, command)  # Get the method corresponding to the command
            if callable(action):
                action()  # Call the method if it exists
            else:
                print("Invalid action.")   
    elif command == "talk":
            print("is talking!")
            inhabitant.talk()
    elif command == "fight" and inhabitant is not None:
        weapon = input("What item do you want to fight with? ")
        if weapon == inhabitant.get_weakness():
            print("You defeated the enemy!")
            current_room.set_character(None)
        else:
            print("You failed to defeat the enemy.")
            print("You have died. Game Over!")
            exit()    
    else:
        print("Invalid command. Please try again.")

    # elif command == "inventory":
    # if inventory:
    #     print("You are carrying:")
    #     for item in inventory:
    #         print(f"- {item.name}")
    # else:
    #     print("Your inventory is empty.")
    # elif command in ["north", "south", "east", "west"]:
    #     if current_room.locked: 
    #         if key in inventory:
    #             print("You unlock the door with the key.")
    #             current_room.locked = False
    #             current_room = current_room.move(command)
    #         else:
    #             print("The door is locked. You need a key.")
    #     else:
    #         current_room = current_room.move(command) 