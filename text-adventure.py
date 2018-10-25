from sys import exit 
from colorama import init
from termcolor import colored

#---------------VARS--------------------

beast_alive = True
dragon_alive = True
sword = False

#--------------ROUTINES------------------

#ROOM 1

def room_1():
  print (colored("\nA Blood-covered Room", 'green'))
  print ("You are in a big room with blood covered walls.")
  print ("It's really dark and all you can see is three doors.")
  print ("They lead east, north, and west.")
  print (colored("Obvious exits: [east, north, west]", 'cyan'))
  print ("What do you do?")

  choice = input("> ");

  if "west" in choice:
    room_2()
  elif "north" in choice:
    room_4()
  elif "east" in choice:
    game_over(""" 
    You carefully go through the narrow passage heading east. 
    After walking for three minutes, you see that it ends with a solid wall. 
    You turn around to get back but you find yourself facing another wall. 
    You have trapped yourself. Without water nor food, you die some days later.""")
  else:
    room_1()

# ROOM 2

def room_2():
  print (colored("\nA Small Passageway", 'green'))
  print ("This room has a really low ceiling and you must crouch to walk.")
  print ("You see a passage leading west and a passage leading north.")
  print ("On the far end of the first one, you can see a bright light.")
  print ("From the second one, a really bad smell emanates.")
  print ("The passage to the east leads back to the first room.")
  print (colored("Obvious exits: [west, north, east]", 'cyan'))
  print ("What do you do?")

  choice = input("> ");

  if "west" in choice:
    game_over("""
    You follow the bright path. As you walk, the light gets 
    brighter and brighter, until you can't see anything. Suddenly you can 
    no longer feel the floor under your feet and, as you fall in a pit of 
    flames, you understand where the light came from. You die screaming in pain.""")
  elif "north" in choice:
    room_3()
  elif "east" in choice:
    room_1()
  else:
    room_2()

# ROOM 3

def room_3():

  global beast_alive
  global sword

  if beast_alive:
    print (colored("\nThe Beast's Den", 'green'))
    print ("As you walk into the room, you understand where the smell came from.")
    print ("The floor is littered with rotting corpses.")
    print ("Suddenly you hear a growl and a huge beast appears in front of you.")
    print ("You see a passage to the east, a flaming " + colored("torch", 'yellow') + " on the ground,")
    print ("a skeleton holding a " + colored("sword", 'yellow') + ", and a hole on the far side of the room.")
    print ("The passage to the south leads back to the second room.")
    print (colored("Obvious exits: [south, east, hole]", 'cyan'))
    print ("What do you do?")

    choice = input("> ")

    if "east" in choice: 
      game_over("""
      As you run towards the east passage, the beast leaps in front 
      of you. You don't have the time to do anything, because the beast opens it's 
      jaws and rips off your head.""")
    elif "torch" in choice:
      print (colored("""
      You take the flaming torch and wave it in front of the beast. 
      It leaps back in fear, stumbles and falls in the hole, disappearing from 
      the room.""", 'yellow'))
      beast_alive = False
      room_3()
    elif "sword" in choice:
      print (colored("""
      You take the sword. Suddenly, it starts emanating a faint glow
      and you feel invincible. Without knowing how, you jump forward and slay
      the beast!""", 'yellow'))
      beast_alive = False
      sword = True
      room_3()
    elif "hole" in choice:
      game_over("""
      You jump in the dark. It wasn't such a good idea, though.
      You start falling in the void, never again hitting a floor. You die days later,
      still falling.""")
    elif "south" in choice:
      room_2()
    else:
      room_3()

  else:
    print (colored("\nThe Beast's Den", 'green'))
    print ("The floor is littered with rotting corpses.")
    print ("You see a passage to the east, a flaming " + colored("torch", 'yellow') + " on the ground,")
    print ("a skeleton holding a " + colored("sword", 'yellow') + ", and a hole on the far side of the room.")
    print ("The passage to the south leads back to the second room.")
    print (colored("Obvious exits: [south, east, hole]", 'cyan'))
    print ("What do you do?")

    choice = input("> ")

    if "east" in choice:
      room_4()
    elif "torch" in choice:
      print (colored("""
      You take the flaming torch and wave it in the air.
  You feel stupid and put it down.""", 'yellow'))
      room_3()
    elif "sword" in choice:
      print (colored("You take the sword.", 'yellow'))
      sword = True
      room_3()
    elif "hole" in choice:
      game_over("""
      You jump in the dark. It wasn't such a good idea, 
      though. You start falling in the void, never again 
      hitting a floor. \n
      You die days later, still falling.""")
    elif "south" in choice:
      room_2()
    else:
      room_3()

# ROOM 4

def room_4():

  global dragon_alive

  if dragon_alive:
    print (colored("\nThe Dragon's Lair", 'green'))
    print ("The room is huge, and for good reasons. It is the home of a dragon.")

    if sword:
      print (colored("""
      Suddenly your sword starts to glow. An unknown force urges you to leap 
      forward and drive the sword in the heart of the dragon. It dies with 
      horrible screams.""", 'yellow'))
      dragon_alive = False
      room_4()
    else:
      print ("There is a passage to the north, one to the east, one to the")
      print ("south and one to the west.")
      print (colored("Obvious exits: [north, east, south, west]", 'cyan'))
      print ("What do you do?")

    choice = input("> ")

    game_over("The dragon leaps in front of you and with a roar begins to breath fire, roasting you alive.")

  else:

    print (colored("\nThe Dragon's Lair", 'green'))
    print ("There is a passage to the north, one to the east, one to the")
    print ("south and one to the west.")
    print (colored("Obvious exits: [north, east, south, west]", 'cyan'))
    print ("What do you do?")

    choice = input("> ")

    if "east" in choice:
      game_over("""
      You follow the east passage until you end up in a little
      room with a desk and a PC on it. A little fellow is typing on the PC and
      suddenly he notices your presence. 'You should not have found me, the
      coder of this game!' he says. 'Now you have to die!' He types something on
      the PC, and you die.""")
    elif "south" in choice:
      room_1()
    elif "west" in choice:
      room_3()
    elif "north" in choice:
      game_over("""
      The passage leads to the surface. You are free! You have won the game!""")
    else:
      room_4()

# START

def start():
  init()
  room_1()

# GAME OVER

def game_over(s):

  global beast_alive
  global dragon_alive
  global sword

  beast_alive = True
  dragon_alive = True
  sword = False

  
  print (colored(s, 'red'))
  print ("Do you want to play again? (y / n)")

  choice = input("")
  # while choice != "y" and choice != "n":
    # choice = input("> ")
  if choice == "y":
    start()
  elif choice == "n":
    exit(0)



#---------------------------MAIN-----------------------------------------

start()