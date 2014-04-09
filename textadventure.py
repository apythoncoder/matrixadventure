import os
import time

#Make a clear screen with timer.
def clearScreen(wait):
	time.sleep(wait)
	os.system('clear') #Change to 'cls' if on Windows,but leave as-is if on Mac. 


class colour:
    Title = '\033[94m'
    Green = '\033[92m'
    Red = '\033[91m'
    Bold = "\033[1m" 
    End = '\033[0m'

#Setup class for the rooms. Make output consistent
class Room(object):

    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options
    
    def __str__(self):
        return colour.Bold + colour.Title + self.name + colour.End + '\n' + self.description + '\n' + colour.Bold + self.options + colour.End

prompt = (colour.Bold + '>> ' + colour.End)
keyOne = False
keyTwo = False
keyThree = False
startGame = True
trollAlive = True
knife = False


def noGo(room):
 	print colour.Red + "There's no door there!" + colour.End
 	clearScreen(3)
 	room()
def locked(room):
 	print colour.Red + "You push and heave, but the door stays locked. Try and find a key." + colour.End
 	clearScreen(3)
 	room()
def didntUnderstand(room):
	print colour.Red + "Sorry, I didn't understand that. Try again." + colour.End
 	clearScreen(1)
 	room()
 	
#Make the rooms
entrance = Room('Entrance', """A cold-floored room. Apart from the empty coat rack, it's scarce. You hear the thunderous rain outside.""", """There is a locked door behind you, and an archway in front of you.""")       
mainHall = Room('Main Hall', """A dusty chandelier hang precariously from the damp ceiling. Two chairs sit in front of an empty fireplace. There are dust sheets over some furniture, tucked away at the side of the room.""", """There is a door on every wall.""") 
empty = Room('An Empty Room', """The steady drip of the rain seeping through the ceiling is the only thing in this room. You hear a loud creaking in the distance. Lightning flashes. You are not alone.""", """To your North and West there is a door.""")
stairs = Room('Stairwell', """A crumbled old staircase, with numerous steps missing, leads to a dark upstairs, the walls framing the silhouettes cast by the lightning. You hear a banging, then a sudden crash. Something is up there...""", """You could go West, up the stairs, or through the doors that are North or East.""")
kitchen = Room('Kitchen', """In the darkness, you can make out counters and tabletops. The floor is littered with broken plates, and saucepans have been knocked to the ground. It seems as if something has been in here.""", """There's a knife rack, and doors on all sides apart from East.""")
library = Room('Library', """Huge bookshelves that go from floor to ceiling surround you. Ripped pages litter the floor. There's a bloodstained book on the centre table""", """Each side has a door.""")
banquetHall = Room('Banquet Hall', """Five long tables fill the room, covered with shattered glasses and cutlery. The centre table has been cracked in half. Above it is a large hole in the ceiling.""", """Each side has a door.""")
toilet = Room('Toilet', """A small, damp room that smells of sewage. The sink has been smashed and the toilet itself has disappeared, ripped from the pipes.""", """The doors to the North and East are open. The one to the West, however, is locked.""")
key3 = Room('Key Room', """You've found a key! It has the word 'Entrance' on it.""", """The only door is East.""")
key2 = Room('Key Room', """You've found a key! It has the word 'Toilet' on it.""", """There are doors to the South and West.""")
bedroom = Room('Bedroom', """A large, Queen-sized bed is in the centre of the room. It has no sheets, only a bare mattress. It smells of mould. You vomit a little.""", """There is a locked door to your East. The doors to the South and West are open.""")
study = Room('Study', """An ornate wooden desk stands infront of you. It has scratches all over it. There is a sheet of paper on its surface.""", """There are doors all around you, apart from North.""")
troll = Room('Troll', """The smell hits you first. The smell of rotting meat. Of human flesh. You look up and see it. The thing in front of you looks inhuman, but it seems intelligent. It moves towards you...""", """Run out the door behind you, or stay and fight!""") 
#Special rooms
deadTroll = Room('Troll', """The troll is dead! Go escape!""", """There are doors to the South and East.""")
end = Room('Finish', """Well done! You escaped. To try again, go North, or to leave, go South down the gravel path.""", """Thanks for playing""")

#Where the magic happens
def entranceChoice():
	global startGame
	if startGame == True:
		startGame = False
	else:
		clearScreen(0)
	print entrance
	direction = raw_input(prompt)

	if direction == 'N':
		mainHallChoice()
	elif direction == 'E':
		noGo(entranceChoice)
	elif direction == 'S':
		if keyThree == True:
			finishGame()
		else:
			locked(entranceChoice)
	elif direction == 'W':
		noGo(entranceChoice)
	else:
		didntUnderstand(entranceChoice)

def mainHallChoice():
	clearScreen(0)
	print mainHall
	direction = raw_input(prompt)

	if direction == 'N':
		libraryChoice()
	elif direction == 'E':
		emptyChoice()
	elif direction == 'S':
		entranceChoice()
	elif direction == 'W':
		stairChoice()
	else:
		didntUnderstand(mainHallChoice)

def emptyChoice():
	clearScreen(0)
	print empty
	direction = raw_input(prompt)

	if direction == 'N':
		kitchenChoice()
	elif direction == 'E':
		noGo(emptyChoice)
	elif direction == 'S':
		noGo(emptyChoice)
	elif direction == 'W':
		mainHallChoice()
	else:
		didntUnderstand(emptyChoice)

def stairChoice():
	clearScreen(0)
	print stairs
	direction = raw_input(prompt)

	if direction == 'N':
		banquetHallChoice()
	elif direction == 'E':
		mainHallChoice()
	elif direction == 'S':
		noGo(stairChoice)
	elif direction == 'W':
		print(colour.Red + 'The stairs collapse, and you fall through a hole, back down to the stairwell.' + colour.End)
		time.sleep(2)
		stairChoice()
	else:
		didntUnderstand(stairChoice)

def kitchenChoice():
	clearScreen(0)
	print kitchen
	global keyOne
	global knife
	direction = raw_input(prompt)

	if direction == 'N':
		if keyOne == True:
			keyTwoChoice()
		else:
			locked(kitchenChoice)
	elif direction == 'E':
		noGo(kitchenChoice)
	elif direction == 'S':
		emptyChoice()
	elif direction == 'W':
		libraryChoice()
	elif direction.startswith("investigate"):
		if knife == False:
			print(colour.Green + "You pick up a knife." + colour.End)
			time.sleep(2)
			knife = True
			kitchenChoice()
		else:
			print("You already have a knife - no need for another")
			time.sleep(3.5)
			kitchenChoice()
	else:
		didntUnderstand(kitchenChoice)

def libraryChoice():
	clearScreen(0)
	print library
	direction = raw_input(prompt)

	if direction == 'N':
		bedroomChoice()
	elif direction == 'E':
		kitchenChoice()
	elif direction == 'S':
		mainHallChoice()
	elif direction == 'W':
		banquetHallChoice()
	elif direction.startswith("investigate"):
		print(colour.Bold + "The book has the title 'How to kill a Troll'. The pages are blank." + colour.End)
		time.sleep(3.5)
		libraryChoice()
	else:
		didntUnderstand(libraryChoice)

def banquetHallChoice():
	clearScreen(0)
	print banquetHall
	direction = raw_input(prompt)

	if direction == 'N':
		studyChoice()
	elif direction == 'E':
		libraryChoice()
	elif direction == 'S':
		stairChoice()
	elif direction == 'W':
		toiletChoice()
	else:
		didntUnderstand(banquetHallChoice)

def toiletChoice():
	clearScreen(0)
	global keyTwo
	print toilet
	direction = raw_input(prompt)

	if direction == 'N':
		trollChoice()
	elif direction == 'E':
		banquetHallChoice()
	elif direction == 'S':
		noGo(toiletChoice)
	elif direction == 'W':
		if keyTwo == True:
			keyThreeChoice()
		else:
			locked(toiletChoice)
	else:
		didntUnderstand(toiletChoice)

def keyThreeChoice():
	clearScreen(0)
	global keyThree
	print key3
	keyThree = True
	direction = raw_input(prompt)

	if direction == 'N':
		noGo(keyThreeChoice)
	elif direction == 'E':
		toiletChoice()
	elif direction == 'S':
		noGo(keyThreeChoice)
	elif direction == 'W':
		noGo(keyThreeChoice)
	else:
		didntUnderstand(keyThreeChoice)

def keyTwoChoice():
	clearScreen(0)
	global keyTwo
	print key2
	keyTwo = True
	direction = raw_input(prompt)

	if direction == 'N':
		noGo(keyTwoChoice)
	elif direction == 'E':
		noGo(keyTwoChoice)
	elif direction == 'S':
		kitchenChoice()
	elif direction == 'W':
		bedroomChoice()
	else:
		didntUnderstand(keyTwoChoice)

def bedroomChoice():
	clearScreen(0)
	print bedroom
	direction = raw_input(prompt)

	if direction == 'N':
		noGo(bedroomChoice)
	elif direction == 'E':
		if keyOne == True:
			keyTwoChoice()
		else:
			locked(bedroomChoice)
	elif direction == 'S':
		libraryChoice()
	elif direction == 'W':
		studyChoice()
	else:
		didntUnderstand(bedroomChoice)

def studyChoice():
	clearScreen(0)
	print study
	direction = raw_input(prompt)

	if direction == 'N':
		noGo(studyChoice)
	elif direction == 'E':
		bedroomChoice()
	elif direction == 'S':
		banquetHallChoice()
	elif direction == 'W':
		trollChoice()
	elif direction.startswith("investigate"):
		print('The paper is a note. It says:')
		print playerName + ", There's a troll in the room to the West that will kill you, unless you have a weapon. \nLots of Love,\nMatrix\nxXx"
		time.sleep(4)
		studyChoice()
	else:
		didntUnderstand(studyChoice)

def trollChoice():
	clearScreen(0)
	global trollAlive
	global knife
	global keyOne

	if trollAlive == True:
		print troll
		direction = raw_input(prompt)

		if direction == 'N':
			clearScreen(0.5)
			if knife == True:
				print("You fight the troll with your knife! He dies, and you remove a key from his neck. It has the word 'kitchen' on it...")
				keyOne = True
				trollAlive = False 
				time.sleep(2)
				trollDead()
			else:
				print(" You didn't have a weapon! The troll kills you. \n\n" + colour.Bold, 'Try again? (y/n)' + colour.End)
				endGame  = raw_input(prompt)
				if endGame == 'n':
					exitGame()
				else:
					restartGame()
		elif direction == 'E':
			bedroomChoice()
		elif direction == 'S':
			toiletChoice()
		elif direction == 'W':
			noGo(trollChoice)
		else:
			didntUnderstand(trollChoice)
	else:
		trollDead()

def trollDead():
	clearScreen(0)
	print deadTroll
	direction = raw_input(prompt)

	if direction == 'N':
		noGo(trollDead)
	elif direction == 'E':
		studyChoice()
	elif direction == 'S':
		toiletChoice()
	elif direction == 'W':
		noGo(trollDead)
	else:
		didntUnderstand(trollDead)	

def exitGame():
	clearScreen(0)
	print('Bye!')
	time.sleep(2)

def restartGame():
	keyOne = False
	keyTwo = False
	keyThree = False
	startGame = True
	trollAlive = True
	knife = False
	entranceChoice()

def finishGame():
	clearScreen(0)
	print end
	direction = raw_input(prompt)

	if direction == 'N':
		restartGame()
	elif direction == 'E':
		noGo(finishGame)
	elif direction == 'S':
		exitGame()
	elif direction == 'W':
		noGo(finishGame)
	else:
		didntUnderstand(finishGame)	
clearScreen(0)
print colour.Bold, colour.Title, "Matrix's Text Adventure\n", colour.End
print colour.Bold, 'Commands:\n', colour.End, '\n N or E or S or W - Travel North/East/South/West\n investigate [object] - Investigate an object'

print('\n\nType your name to proceed.')
playerName = raw_input(prompt)
clearScreen(0.5)

print """You come to your senses. Reaching up to feel your head, you find a large lump. You have an intense headache, but it passes as your vision clears. You're lying on your back. It's dark, and the only source of light is the full moon you can see through a high window. Your wrists are raw, as if they had been rubbed by a thick rope. You stand up shakily onto your feet. In the distance, you hear thunder."""
time.sleep(4)

#Start it!
entranceChoice()