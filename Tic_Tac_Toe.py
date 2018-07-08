from IPython.display import clear_output

print('\n'*100)
# How to display board and mapping keypad

def display_board(board):
  print('\n'*100)
  print('   |   |')
  print(' ' + board[7] + ' |' + ' ' + board[8] + ' |' + ' ' + board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' |' + ' ' + board[5] + ' |' + ' ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[1] + ' |' + ' ' + board[2] + ' |' + ' ' + board[3])
  print('   |   |')
  
# This is a test to view the board
    
# test_board = ['x','o','x','o','x','o','x','x','x','x']
# display_board(test_board)

# Choosing x or o and then returning who is x and o.

def player_input():
  marker = ''
  while marker != 'x' or marker != 'o':
    marker = input('Please Choose X or O: ')
    if marker == 'x':
      return('X', 'O')
    else:
      return('O', 'X')

# Input for assigning a mark on the board

# print(player_input())

def place_marker(board, marker, position):
  board[position] = marker

#Testing where marker is on the board

# place_marker(test_board,'$',5)
# display_board(test_board)

# Code to check when a game is won. All possible outcomes of a winning game. 

def win_check(board,mark):
  return((board[7]==mark and board[8]==mark and board[9]==mark or # top row
  board[4]==mark and board[5]==mark and board[6]==mark or # middle row
  board[1]==mark and board[2]==mark and board[3]==mark or # bottom row
  board[7]==mark and board[4]==mark and board[1]==mark or # left column
  board[8]==mark and board[5]==mark and board[2]==mark or # middle column
  board[9]==mark and board[6]==mark and board[3]==mark or # right column
  board[7]==mark and board[5]==mark and board[3]==mark or # left diagnol
  board[9]==mark and board[5]==mark and board[1]==mark)) # right diagnol

# Test to check if code works. This test needs to be in conjuction with test_board.

# print(win_check(test_board,'x'))

# Code to decide who goes first

import random
def choose_first():
  if random.randint(0,1)==1:
    return 'Player 1 Goes First'
  else:
    return 'Player 2 Goes First'

# print(choose_first()) 

# Code to check if their is open board space/available. 

def space_check(board, position):
  return board[position] == ' '

# Code to check if a board is full.

def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i):
      return False
  return True

# Code for player to choose next position, and to check if it is a free position.

def player_choice(board):
  position = 0

  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
    position = int(input("Choose your next position: (1-9)"))
  
  return position

# Code to ask player if they want to play again.

def replay():
  return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

# Full code to run the game

print('Welcome to Tic Tac Toe!!!')

while True:
  the_board = [" "]*10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn)

  play_game = input("Are you ready to play? Enter Yes or No:")

  if play_game.lower()[0] == 'y':
    game_on = True
  else:
    game_on = False

  while game_on:
    if turn == "Player 1":
      # Player1 turn

      display_board(the_board)
      position = player_choice(the_board)
      place_marker(the_board, player1_marker,position)

      if win_check(the_board,player1_marker):
        display_board(the_board)
        print("Congratulations, Player 1 has won!")
        game_on = False

      else:
        if full_board_check(the_board):
          display_board(the_board)
          print("The game is a draw!")
          break
        else:
          turn = "Player 2"
    
    else:
      #player 2 turn
        display_board(the_board)
        position = player_choice(the_board)
        place_marker(the_board,player2_marker,position)

        if win_check(the_board,player2_marker):
          display_board(the_board)
          print("Congratulations, Player 2 has won!")
          game_on = False
        
        else:
          if full_board_check(the_board):
            print("The game is a draw!")
            break
          else: 
            turn = "Player 1"
  if not replay():
    break

##############

