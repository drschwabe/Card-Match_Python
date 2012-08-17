from time import sleep
from random import shuffle

#Card Match

#determine the value of each card 
cardValues = ['cow', 'cow', 'cow', 'cow', 'eagle', 'eagle', 'eagle', 'eagle', 'ladybug', 'ladybug', 'ladybug', 'ladybug', 'gold', 'gold', 'ruby', 'ruby', 'diamond', 'diamond']

#shuffle the cards
shuffle(cardValues)

#flip them all face down
cardSide = ['face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down', 'face down']


#give the user only 3 possible chances (a chance is not used if a match is made)
chances = 4;

#if the user wins 9 matches they will win
matches = 0;

#let the user pick a card!

print "\n#### Welcome to Card Match ####\n"

def pickCard() :
	global selectedCardNumber;
	global previousSelectedCardNumber;
	selectedCard = raw_input("===\nPlease choose a card from 0 to 17\n");
	selectedCardNumber = int(selectedCard);
	sleep(1);

	print "\nYou chose card", selectedCardNumber; 
	print "That card is currently", cardSide[selectedCardNumber]; 


	if cardSide[selectedCardNumber] == "face down" :
		cardSide[selectedCardNumber] = "face up";
		print "We will now turn it over to see what it is...\n";
		sleep(1);
		print "The card value is: ", cardValues[selectedCardNumber];
		print "\n"
		sleep(1);
		pickAgain();
	else :  #if the card is faceup, make the user try again
		print "That card is already flipped over! Its your ", cardValues[selectedCardNumber];
		pickCard();


#let the user pick another card and see if they match

def pickAgain() :
	global selectedCardNumber;
	global previousSelectedCardNumber;
	global chances;
	global matches;
	previousSelectedCardNumber = selectedCardNumber;
	selectedCard = raw_input("===\nPlease choose another card. From 0 to 17\n");
	selectedCardNumber = int(selectedCard);
	sleep(1);

	print "\nYou chose card", selectedCardNumber; 
	print "That card is currently", cardSide[selectedCardNumber]; 

	if cardSide[selectedCardNumber] == "face down" :
		cardSide[selectedCardNumber] = "face up";
		print "We will now turn it over to see what it is...\n";
		sleep(1);
		print "The card value is: ", cardValues[selectedCardNumber];
		if cardValues[selectedCardNumber] == cardValues[previousSelectedCardNumber] :
			print "Wow, you got a match!\a\n\n";
			matches = matches + 1;
			sleep(1);
			if matches == 9 :
				print "You won the game!\a\a\a\a\a";
			else :
				pickCard();
		else :
			print "Sorry, that was not a match :(\n\n";
			chances = chances -1;
			#reset the selected cards
			cardSide[selectedCardNumber] = "face down"; 
			cardSide[previousSelectedCardNumber] = "face down";
			print "You have %d chances left" % chances;
			if chances == 0 :
				print "Game over";
				sleep(1);
			else :
				pickCard();

	else : 
		print "That card is already flipped ovenr! Its your ", cardValues[selectedCardNumber];
		selectedCardNumber = previousSelectedCardNumber; #reset the selectedCard
		pickAgain();

pickCard();