from getpass import getpass as input

print("Rock Papers Scissors Game!")
print()

print("First to 3 wins!")
print("Select your move by pressing (R, P or S)")
print()

player1_score = 0
player2_score = 0

while True:
  player1Move = input("Player 1 > ")
  if player1Move == "R" or player1Move == "P" or player1Move == "S":
    print("Player 1 Chosses!")
  else:
    print("Invalid Move Player 1")

  player2Move = input("Player 2 > ")
  if player2Move == "R" or player2Move == "P" or player2Move == "S":
    print("Player 2 Choses!")
  else:
    print("Invalid Move Player 2")
    
#Results of the choices
  if player1Move == "R":  
    if player2Move == "R":
      print("You both picked Rock, draw!")
    elif player2Move == "S":
      print("Player 1 smashed Player 2's Scissors into dust with their Rock!")
      player1_score += 1
    elif player2Move == "P":
      print("Player 1's Rock is smothered by Player 2's Paper!")
      player2_score += 1  
      
  elif player1Move == "P":
    if player2Move == "R":
      print("Player 2's Rock is smothered by Player 1's Paper!")
      player1_score += 1
    elif player2Move == "S":
      print("Player 1's Paper is cut into pieces by  Player 2's Scissors!")
      player2_score += 1
    elif player2Move == "P":
      print("Two bits of paper flap at each other.  Dissapointing. Draw.")

  elif player1Move == "S":
    if player2Move == "R":
      print("Player 2's Rock makes metal-dust out of Player 1's Scissors")
      print()
      player2_score += 1
    elif player2Move == "S":
      print( "Scissors bounce off each other like a dodgy sword fight! Draw")
      print()
    elif player2Move == "P":
      print( "Player 1's Scissors make confetti out of Player 2's paper!")
      print()
      player1_score += 1

#Ending Winner
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score == 3 or player2_score == 3:
    print ( "Thanks for playing!")
    exit()
  else:
    continue