'''
Blackjack:
Computer plays the role of dealer.

1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again
'''

import random

suits = ('Hearts','Diamonds','Spade','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}



class Bankroll:
	'''
	Bankroll class with initial balance 100.
	Option to modify balance by adding more chips.
	Option to place bet. If bet is insufficient - ask for more balance or to reduce bet.
	'''
	def __init__(self,balance=100):
		self.balance = balance



	def modify_balance(self):
		while True:
			try:
				add_balance = int(input("How many chips to add? "))
			except:
				print("Invalid input")
			else:
				self.balance += add_balance
				print(f"Balance added.\nNew Balance: {self.balance}")
				break
		
	def __str__(self):
		return f"Balance:  {self.balance}"

	def place_bet(self):
		while True:		
			try:
				bet_amount = int(input("Place your bet: "))
			except:
				print("Invalid input")
			else:
				if bet_amount > self.balance:	
					choice = input("Not enough balance. Add Balance (A) or Reduce Bet (R)?").upper()
					if choice == 'R':
						continue
					if choice == 'A':
						self.modify_balance()
					

				else:
					self.balance -= bet_amount
					print('Bet Accepted')
					break


class Card:
	'''
	Defines a Card Class
	'''
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank


	def __str__(self):
		return f"{self.rank}  of   {self.suit}"


class Deck:
	'''
	Defines a Deck Class
	'''
	def __init__(self):
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				self.all_cards.append(Card(suit,rank))

	def __len__(self):
		return len(self.all_cards)

	def draw_card(self):
		return self.all_cards.pop(0)

	def shuffle(self):
		while True:
			try:
				n = int(input("How many times do you want to shuffle?"))

			except:
				print("Invalid input. Enter an integer")

			else:
				for i in range(n):
					random.shuffle(self.all_cards)
				break


def disp_hands(turn,game_round):
	'''
	Displays the current hand depending on game round.
	If it is player's turn - dealer's first card is hidden. If it is dealer's turn all cards are displayed.
	'''
	print(f"Game Round : {game_round}")
	print("\nPlayer Hand")
	for ele in range(len(player_hand)):
		print(player_hand[ele])

	print("\nDealer Hand")
	if turn == 1:
		print(dealer_hand[0])
		print("Unknown Card\n____________")
	
	elif turn == 2:
		for eletwo in range(len(dealer_hand)):
			print(dealer_hand[eletwo])
		print("\n____________")


def check_sum(whose_hand):
	'''
	Calculates current value of hand.
	'''
	sum = 0;

	#Add sum of values of cards.
	for ele in range(len(whose_hand)):
		sum += values[whose_hand[ele].rank]
	return sum 

'''
Main Game
'''

#Creates a new deck
new_deck = Deck()

#Shuffles the deck
new_deck.shuffle()

#Creates a new bankroll
player_bank = Bankroll()

#Player chooses a bet value
player_bank.place_bet()

#Creating player and Dealer hands
dealer_hand = []
player_hand = []

#Deal two cards each to player and dealer
for i in range(2):
	player_hand.append(new_deck.draw_card())
	dealer_hand.append(new_deck.draw_card())

turn = 1 #Game begins at player's turn.
game_round = 1
game_on = True
disp_hands(turn,game_round)
#Display the cards at the beginning


##Player's Turn
##while condition is for running the player's round
while game_on == True:
	if turn == 1:
		move = input("Choose Hit Or Stay").upper()
		if move == "HIT":
			game_round += 1 
			#Draw a Card
			player_hand.append(new_deck.draw_card())
			#Display Hands
			disp_hands(turn,game_round)
			player_sum = check_sum(player_hand)
			if player_sum > 21:
				print("Bust! Dealer wins the game!")
				break
				game_on = False

		elif move == "STAY":
			game_round +=1 
			turn = 2
			break
		else:
			print("Invalid input") 

##Dealer's Turn
if turn == 2:
	dealer_sum = check_sum(dealer_hand)
	while dealer_sum < 17:
		dealer_hand.append(new_deck.draw_card())
		print("Dealer draws a card")
		game_round += 1
		#Display Hands
		disp_hands(turn,game_round)
		dealer_sum = check_sum(dealer_hand)
		print(f"Sum is {dealer_sum}")

dealer_sum = check_sum(dealer_hand)
player_sum = check_sum(player_hand)
if dealer_sum > 21:
	print('Bust! Player wins the game!')
elif dealer_sum >= player_sum:
	print('Dealer wins the game!')
elif player_sum <=21 and player_sum > dealer_sum:
	print('Player wins the game!')

