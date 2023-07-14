# Gambler's Ruin
# Python program written by Sean Luciw July 2023
# inspired by the topic in Udemy course

import random

global player_one_coins
global player_two_coins
global player_one_coins_start
global player_two_coins_start
global num_flips
global num_heads
global num_tails
global num_rounds_player_one_leading
global num_rounds_player_two_leading
global num_rounds_tied
global display_style # 0 or 1

def function_introduction():
	print()
	print('GAMBLER\'S RUIN, a Python program by Sean Luciw' )
	print()
	print('A well-known concept called Gambler\'s Ruin says that a gambler with finite wealth will eventually lose all their winnings against an opponent with infinite wealth (the casino, for example) during a repeated fair bet process such as coin flipping. This program allows the user to adjust the starting wealth of both opponents, and then flips coins automatically. Heads means Player 1 takes a coin from Player 2, and vise-versa, until a player runs out of coins and the other player wins. A report is given at the end of the process.')

def function_flip_coin():
	global num_heads
	global num_tails
	coin_flip = random.choice([-1, 1])
	if (coin_flip == 1):
		if (display_style == 1):
			print('Heads. Player 1 takes coin.')
		else:
			print('H ', end='')
		num_heads +=1
	elif (coin_flip == -1):
		if (display_style == 1):
			print('Tails. Player 2 takes coin.')
		else:
			print('T ', end='')
		num_tails +=1
	return coin_flip
	
def function_get_input():
	global player_one_coins
	global player_two_coins
	global player_one_coins_start
	global player_two_coins_start
	global display_style
	print()
	msg_input_player_one_start_amt = 'How many coins for Player 1 at start? '
	msg_input_player_two_start_amt = 'How many coins for Player 2 at start? '
	player_one_coins_start = int(input(msg_input_player_one_start_amt))
	player_two_coins_start = int(input(msg_input_player_two_start_amt))
	player_one_coins = player_one_coins_start
	player_two_coins = player_two_coins_start
	msg_input_select_display_style = 'Choose display style for coin flips (Enter = brief, 1 = detailed)?'
	display_style_input = input(msg_input_select_display_style)
	if (display_style_input):
		display_style = int(display_style_input)
	else:
		display_style = 0 # 0 or 1 default

def function_play_game():
	global player_one_coins
	global player_two_coins
	global num_flips
	global num_heads
	global num_tails
	global num_rounds_player_one_leading
	global num_rounds_player_two_leading
	global num_rounds_tied
	num_flips = 0
	num_heads = 0
	num_tails = 0
	num_rounds_player_one_leading = 0
	num_rounds_player_two_leading = 0
	num_rounds_tied = 0
	print()
	print()
	print('FLIPPING COINS:')
	while True:
		if (player_one_coins > 0) and (player_two_coins > 0):
			num_flips += 1
			if (display_style ==1):
				print()
				print('Round:', num_flips)
			this_coin_flip = function_flip_coin()
			player_one_coins += this_coin_flip
			player_two_coins -= this_coin_flip
			if (display_style == 1):
				print('Player 1 now has', player_one_coins, 'coins.')
				print('Player 2 now has', player_two_coins, 'coins.')
			if (player_one_coins > player_two_coins):
				num_rounds_player_one_leading +=1
			elif (player_one_coins < player_two_coins):
				num_rounds_player_two_leading +=1
			else:
				num_rounds_tied +=1
		else:
			break

def function_summary():
	print()
	print()
	print('GAME REPORT:')
	print()
	if (player_one_coins == 0):
		print('Player 2 wins and keeps all', player_two_coins ,'coins!')
	elif (player_two_coins == 0):
		print('Player 1 wins and keeps all', player_one_coins ,'coins!')
	else:
		print('error')
	print('Player 1 started with', player_one_coins_start, 'coins.')
	print('Player 2 started with', player_two_coins_start, 'coins.')
	print('Total number of coin flip rounds:', num_flips)
	print('Heads was flipped', num_heads, 'times.')
	print('Tails was flipped', num_tails, 'times.')
	print('Coin-flip ratio was', round(100*(min(num_heads, num_tails)/max(num_heads, num_tails)), 2), 'percent fair.')
	print('Player 1 was ahead for', num_rounds_player_one_leading, 'rounds.')
	print('Player 2 was ahead for', num_rounds_player_two_leading, 'rounds.')
	print('The score was tied for', num_rounds_tied, 'rounds.')
	print()
	

# MAIN LOOP
function_introduction()
function_get_input()
function_play_game()
function_summary()

#