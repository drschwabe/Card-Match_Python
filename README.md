Card-Match
==========

Simple memory game based on the Super Mario Bros 3 minigame. 

Game logic, in a nutshell: 
18 cards are layed out on the table.  
The player can select up to 2 cards. These are "flipped up" temporarily. 
If the two cards are a match, those cards remain flipped up for the duration of the game.
If the player matches all cards they win. 
To make it easier, they get x number of chances to make new pairs. 

How I tackled it, in a nutshell: 
Nov 25, 2012
15:49 - There are only 2 functions: one to handle player input, and one to handle the bulk of the logic.
I used 2 arrays to store data: one for the status of each card (face down, face up)...
and one for the values of each card (ladybug, gold, mushroom, etc). 
After the game starts, the 'cards' are shuffled and the user is prompted to make a selection. 
Their selection will be a number, which can be used as a key for both arrays. 
Then I simply maintain a limited set of variables or "switches" ...
to manage execution flow between the player and ai functions. 
Difficulty can be adjusted by tweaking the number of chances or the values of the cards...
More chances means the player can keep trying.  More variety of card values = less odds of getting a match. 

---Derrick