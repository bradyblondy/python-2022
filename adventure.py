#import all the functions from adventurelib
from adventurelib import *

#rooms
room.Items = Bag()

space = Room("you are drifting in space. You se a spaceship")
airlock = Room("you are in an airlock")
cargo = Room("you are in the cargo bay")
docking = Room("you are in the docking bay")
hallway = Room("you are in a hallwaywith four exits")
bridge = Room("you stand on the bridge of the ship. There is a dead body.")
mess = Room("you are in the kitchen/dining area")
quaters = Room("you are in the crew quarters. there is a locker.")
escape = Room("you are in an Escape pod")

#room connections
docking.west = cargo
hallway.north = cargo
hallwa.east = bridge
hallway.south = mess
hallway.west = airlock
bridge.south = escape
mess.west = quarters
quarters.north = airlock

#items
Items.description = "" #make sure each item has a description
keycard = Item("Ared keycard", "keycard","card","key","red","keycard")
keycard.description = you look at the keycard and see that it is labelled, excape pod

note = Item("A scribbled note","note","paper","code")
note.description = "you look at the note. The numbers are 2,3,5,4."

#add items to room
quarters.item.add(note)

#variables
current_room = space
inventory = bag()
body_searched = False
used_keycard = False

#blinds
@when("jump")
def jump():
	print("you jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("you haul yourself into the airlock")
		current_room = airlock
	else:
		print("there is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel ")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits has
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"you go {direction}")
		print(current_room)
	else:
		print("you can't go that way")

@when("look")
def look():
	print(current_room)
	print(f"ther are exits to the ",",".join(current_room.exits()))
	if len(current_room,item) > 0:
		print("you also see:")
		for item in current_room.items:
			print(item)

@when("get ITEM")
@when("take ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no item
	if item in current_room.item:
		t = current_room.item.take(items)
		inventory.add(t)
		print(f"you pick up the {item}")
	else:
		print(f"you don't see a {item}")

@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	if current_room == bridge and body_searched == False:
		print("you search the body and a red keycard falls to the floor")
		current_room.item.add(keycard)
		body_searched = True 
	elif current_room == bridge and body_searched == False:
		print("You already searched the body")
	else:
		print("There is no body here to search")

@when("use ITEM")
def use(item):
	if item == keycard and current_room == bridge:
		print("You use the keycard and the escape pod slides open")
		print("The escape pod stands open to the south")
		used_keycard = True
		bridge.south = escape
	else:
		print("You can't use that here")



@when("type c"
#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#THE MAIN FUNCTION
def main():
	print(current_room)
	start()
	#start the main loop

main()