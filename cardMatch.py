#### Card Match alpha2 Python ####

from random import shuffle
from sys import exit
from time import sleep

#Establish variables: 
spark = "";
beginSwitch = False;
checkSelectionSwitch = False;

firstCard = 0;
secondCard = 0;
choosingFirstCard = False;
choosingSecondCard = False;

cardValues = [];
cardStatus = [];

matches = 0;
chances = 6;

#Function to handle player input: 
def playerHandler(): 
	global spark;
	global beginSwitch;
	global checkSelectionSwitch;
	global firstCard;
	global secondCard;
	global choosingFirstCard;
	global choosingSecondCard; 

	#Player input initiates execution flow so let's refer to it as the "spark": 
	spark = raw_input();

	if(spark == "begin" or spark =="b"):
		print "Game starts\n\n"; 
		#Hit the beginSwitch...
		beginSwitch = True;
		#and connect to the ai function: 
		aiHandler();

	if(choosingFirstCard == True):
		#Convert the player's input from string to an integer so it can be used as an array key:
		firstCard = int(spark);
		checkSelectionSwitch = True;
		aiHandler();

	if(choosingSecondCard == True):
		selectedCard = firstCard;
		secondCard = int(spark);
		print ("the second card is " + str(secondCard));
		checkSelectionSwitch = True;
		aiHandler();

#Function to compute most logic: 
def aiHandler():
	global spark;
	global beginSwitch;
	global checkSelectionSwitch;
	global firstCard;
	global secondCard;
	global choosingFirstCard;
	global choosingSecondCard; 

	global cardValues;
	global cardStatus 
	global chances;
	global matches;

	if(beginSwitch == True):
		#Set card values, their status, and then shuffle them. 
		cardValues = ['cow','cow','cow','cow','eagle','eagle','eagle','eagle','ladybug','ladybug','ladybug','ladybug','gold','gold','ruby','ruby','diamond','diamond'];
		cardStatus = ['face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down','face down'];		
		shuffle(cardValues);

		#[graphics] Display a 'table' of cards for the user: 
		print(cardStatus);

		#[graphics] Prompt the user to make a selection...
		print("\nPlease choose a card from 0 to 17");
		#activate "choostingFirstCard"...
		choosingFirstCard = True;
		#turn off beginSwitch...
		beginSwitch = False;
		#Fire back to the player input function: 
		playerHandler();

	if(checkSelectionSwitch == True):

		if cardStatus[firstCard] == "face down" :
			#If the firstCard is face down, we know this is their first selection.
			#[graphics] Inform the user we will flip over the card now: 
			print "\nYou chose card", firstCard; 
			print "We will now turn over that card to see what it is...\n";

			#Flip the card...
			cardStatus[firstCard] = "face up";
			#[graphics] Create a 1 second delay before revealing anything: 
			sleep(1);

			#[graphics] Reveal the value of the card to the user: 
			print "The card value is: " + cardValues[firstCard] + "\n";
			sleep(1);

			print cardStatus;
			print "\nChoose another card from 0 to 17 (to match your: " + cardValues[firstCard] + ")";
			choosingFirstCard = False;
			choosingSecondCard = True;
			playerHandler()

		elif cardStatus[secondCard] == "face down":
			print "\nYou chose card", secondCard;
			print "Lets see what it is...\n"
			cardStatus[secondCard] = "face up"; 
			sleep(1);

			print "The card value is: ", cardValues[secondCard];
			sleep(1);

			if (cardValues[firstCard] == cardValues[secondCard]):
				print "You got a match!\a\n\n";
				matches = matches + 1;
				#Set the status of the card to the value of the card (flipped up permanently):
				cardStatus[firstCard] = cardValues[firstCard];
				cardStatus[secondCard] = cardValues[secondCard];

				if matches == 9 :
					print cardStatus
					print "You won the game!\a\a\a\a\a\n";
					exit();

				else: 
					print "You have this many matches: " + str(matches) + " (of 9 total required)\n";
					print cardStatus;
					print "\nSee if you can match another pair.  Choose a card from 0 to 17:"
					choosingFirstCard = True;
					playerHandler();

			else :
				print "\nSorry, that was not a match.  Try again.";
				chances = chances -1;
				print "(You have this many chances left: " + str(chances) + ")\n"; 
				cardStatus[firstCard] = "face down";
				cardStatus[secondCard] = "face down";

				if chances == 0 :
					print "Game over";
					sleep(1);
					exit();

				else:
					print cardStatus;
					choosingFirstCard = True;
					playerHandler();

		else :
			print "That card is already flipped!";
			sleep(1);
			print "Choose another card from 0 to 17:"
			playerHandler();


print "\n#### Welcome to Card Match ####\n(type 'B' to Begin)";

playerHandler();