##########################################################
## ADVENTURE GAME STARTS HERE
##########################################################
import random
from adven import *

# start by creating the game system
game = Game("Zoo Escape")

# define and describe a couple of locations
foodcourt = game.new_location("Food Court {e}","The air is damp and your arms ache from trying to find your way out of the old abandoned zoo.  It must have been hours since you last saw anyone, not even the overbearing foreman.\nYou decide checking to see if anyone is sharing in your bad luck is enough cause to take a break.\n")
tunnel = game.new_location("Tunnel {e, w}","You don't believe you will ever get used to this oppressive heat this far into the mountain.  You expect to find someone around the upcoming bend in the path.\n")
tunnelbend = game.new_location("A Bend in the Path {e, w}", "You start talking about how poor your luck is as you round the turn hoping to see that someone is having the same streak of bad luck as you.\nNo one is in sight.  You see a safari hat that is on the ground and food scraps in various piles.  There is also a busted open animal cage that looks like it had contained a tiger.\n")
intersection = game.new_location("Path Intersection {n,e,s,w}", "You have come to a 4-way intersection in the tunnel, foot prints and forgotten souvenirs lead in all directions.\n")
path = game.new_location("Path {n,s}", "You head north from the intersection, hoping to find some fellow tourists.  Worry starts to creep into your head.\n")
path = game.new_location("Path {n,s}", "You head north from the intersection, hoping to find some fellow tourists.  Worry starts to creep into your head.\n")
path = game.new_location("Path {e,w}", "You head north from the intersection, hoping to find some fellow tourists.  Worry starts to creep into your head.\n")
giraffe pen = game.new_location("Giraffe Pen {n,s}", "Continuing north from the intersection, you notice some footprints on the ground leading further into the tunnel, getting darker and darker.\n")
fish tank path = game.new_location("Fish Tank Path {n,s}", "It is getting oppressively dark as you notice the path climbing upwards.  You'll have to find a lightsource to continue forward.\n")
reptile room = game.new_location("Reptile Room {s, down}", "Lighting the flare, you are able to continue to the end of this section of path.  You slowly approach a snake enclouser that has fell into disrepair.\nYou notice that there is many small and large snakes slithering aroung across the hall, next to them is an air vent that has been ripped of the wall. Is it a way out?\n")
air vent1 = game.new_location("Air Vent {up, n}", "As you crawl further and further into the vent, you hear a faint voice north of you.\n")
air vent2 = game.new_location("Air Vent {n, s}", "As you keep crawling forward the voice keeps getting louder.\n")
air vent3 = game.new_location("Air Vent {n, s}", "There is an opening in the vent, and you peak your head through to see two men talking about how they are getting ready to go out and hunt the other lost tourists.\n")
air vent4 = game.new_location("Air Vent {down, s}", "You climb out of the vent as the men leave and look around the room they were in. There is guns, food, ammo, and backpacks. You take a pack and pack it with all the food, ammo and most of the guns.\n")
secret room = game.new_location("Secret Room {n, up}", "As you grab all the new equipment you hear the men coming back to the room.\n")
air vent5 = game.new_location("Air Vent {n, s}", "Just as you get back into the Air Vent with all of your new supplies, you start to see a light coming from the other end of the vent.\n")
air vent6 = game.new_location("Air Vent {n, s}", "As you approach the end of the vent you start to see sunlight beeming through the vent gate.\n")
air vent exit = game.new_location("Air Vent Exit {n, s}", "You finally reach the end of the vent and you see what it seems like the parking lot of the zoo with a lot of men that look similar to the men you saw in the secret room, and they all are heavily armed.\n")
parking lot1 = game.new_location("Parking Lot {n}", "You breack open the vent gate and crawl out, but somehow none of the men notice you.\n")
parking lot2 = game.new_location("Parking Lot {n}", "As you notice the men not seeing you, you begin to run to the gate of the Parking Lot.\n")
parking lot gate = game.new_location("Parking Lot Gate {n}", "After running you reach the gate but it is locked. You tug on the gate door hoping that if you tugged on it hard enough it would open. As you are tugging you hear a loud bang and then then the lock fell off its hinges, opening the door.\n")
open world = game.new_location("Open World {n}", "After the door is opened you start to sprint out into the world and you finally have escaped the zoo. While you are running you turn to see that all of those men that were in the zoo and in the parking lot were the police trying to rescue you and any others trapped.\n")

# room connections
game.new_connection("Path", deadend, path, [EAST], [WEST])
game.new_connection("Path", path, pathbend, [EAST], [WEST])
game.new_connection("Path Intersection", pathbend, intersection, [EAST],[WEST])
game.new_connection("Path", intersection, path, [NORTH],[SOUTH])
game.new_connection("Path", intersection, path, [SOUTH], [NORTH])
game.new_connection("Path", intersection, path, [EAST], [WEST])
game.new_connection("Giraffe Pen", path, giraffe pen, [NORTH, FORWARD], [SOUTH, BACK])
game.new_connection("Fish Tanks", giraffe pen, fish tank path, [NORTH, FORWARD], [SOUTH, BACK])
game.new_connection("Dark Reptile Room", fish tank path, reptile room, [NORTH, FORWARD], [SOUTH, BACK])
game.new_connection("Air Vent", reptile room, air vent1, air vent2, air vent3, air vent4, air vent5 [NORTH, FORWARD], [SOUTH, BACK], [DOWN])
game.new_connection("Secret Room", air vent4, secret room, air vent5 [NORTH, FORWARD], [UP])
game.new_connection("Air Vent", secret room, air vent5, air vent6 [NORTH, FORWARD], [SOUTH, BACK])
game.new_connection("Air Vent Exit", air vent6, air vent exit [NORTH, FORWARD], [SOUTH, BACK])
game.new_connection("Parking Lot", air vent exit, parking lot1, parking lot2 [NORTH, FORWARD])
game.new_connection("Parking Lot Gate", parking lot2, parking lot gate [NORTH, FORWARD])
game.new_connection("Open World", parking lot gate, open world [NORTH, FORWARD])

# Now let's ad
#Function to feed the Tiger, keep in mind that while this either feeds the tiger or not, you could call the Die("you die") function to kill the player, or the player.terminate() or tiger.terminate() function!
#def feed_tiger(game, d some items, by providing a single word name and a longer
# description.
piece = deadend.new_object("Piece of Food", "Pieces of food have fallen on to the ground of the zoo from the animals that were left unattended")
piece = deadend.new_object("Piece of Food", "Pieces of food have fallen on to the ground of the zoo from the animals that were left unattended")
piece = deadend.new_object("Piece of Food", "Pieces of food have fallen on to the ground of the zoo from the animals that were left unattended")
cage = tunnelbend.add_object(Container("tigercage", "There is a standard issue tigercage, hopefully the tiger it carried is still around."))
hat = tunnelbend.new_object("Safari Hat", "A well-cared for hat, it's obvious its owner cared about his job, which makes you wonder why they left it on the ground.")
flare = giraffe pen.new_object("flare", "This flare still holds some heat from when it was lit, someone just recently doused it.")
cage.new_object("tiger food", "you see some tiger food on the bottom of the cage.")
food = air vent4.new_object("Food", "All this food is from the food bufet from across the street, you better not eat it all at once.")
gun = air vent4.new_object("Gun", "These weapons are made to kill, you might want to make sure you shoot the right people.")
ammo = air vent4.new_object("Ammo", "These clips look like they fit the rifle you took.")
backpack = air vent4.new_object("Backpack", "You should put all the new supplies you found into this pack.")

# NPC Characters
tiger = Animal("tiger")
tiger.set_location(path)
tiger.set_allowed_locations = ([path, intersection, path, giraffe pen, fish tank path, path, tunnelbend, path, foodcourt])
game.add_actor(tiger)

#Function to feed the Tiger, keep in mind that while this either feeds the tiger or not, you could call the Die("you die") function to kill the player, or the player.terminate() or tiger.terminate() function!
def feed_tiger(game, thing):
    if not "tiger food" in game.player.inventory and "piece of food" in game.player.inventory:
        game.output("While looking at all the food scraps on the floor, the tiger walks up and eats some.You reach into your pocet and grab some of the tiger food found in the cage.")
        tiger.terminate()
    elif not "Tiger food" in game.player.inventory:
        game.output("Feed the tiger with what?")
    else:
        game.output("You sprinkle some tiger food onto your palm and after a few minutes the tiger comes up to you and starts to eat the food out of your hand before it goes back to wandering the zoo.")

tiger.add_phrase("feed tiger", feed_tiger)


# And we can make the flare required to proceed down the dark reptile room
reptile room.make_requirement(flare)


player = game.new_player(deadend)


game.run()
