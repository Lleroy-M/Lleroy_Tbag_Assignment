from room import Room
from character import Enemy

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining hall") 

dave = Enemy("Dave", "A smelly Zombie")
dave.set_conversation("hi im Dave i wont bite you!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shining gold plate")
dining_hall.set_description("A large room with ornate descriptions")

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
    elif command == "talk":
            print("is talking!")
            inhabitant.talk()
    elif command == "fight" and inhabitant is not None:
        weapon = input("What item do you want to fight with? ")
        if weapon == inhabitant.get_weakness():
            print("You defeated the enemy!")
            current_room.remove_character()
        else:
            print("You failed to defeat the enemy.")
    else:
        print("Invalid command. Please try again.")
