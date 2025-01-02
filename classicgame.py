from getpass import getpass as input

print("Rock Papers Scissors Game!")
print()

print("First to 3 wins!")
print("Select your move by pressing (R, P or S)")
print()

player1Score = 0
player2Score = 0

while True:
  print()
  player1 = input("Player 1 > ")
  if player1 == "R" or player1 == "P" or player1 == "S":
    print("Player 1 selected")
    print()
  else:
    print("Invalid selection Player 1")
    break
  player2 = input("Player 2 > ")
  if player2 == "R" or player2 == "P" or player2 == "S":
    print("Player 2 selected")
    print()
  else:
    print("Invalid selection Player 2")
    break

  if player1 == "R" and player2 == "R":
      print("It's a tie!")
      print()
  elif player1 == "R" and player2 == "P":
      print("Player 2's Paper covers Rock and wins!")
      print()
      player2Score += 1
  elif player1 == "R" and player2 == "S":
      print("Player 1's Rock smashes Scissors and wins!")
      print()
      player1Score += 1
      
  elif player1 == "P" and player2 == "R":
      print("Player 1's Paper covers Rock and wins!")
      print()
      player1Score += 1
  elif player1 == "P" and player2 == "P":
      print("It's a tie!")
      print()
  elif player1 == "P" and player2 == "S":
      print("Player 2's Scissors cuts Paper and wins!")
      player2Score += 1

  elif player1 == "S" and player2 == "R":
      print("Player 2's Rock smashes Scissors and wins!")
      print()
      player2Score += 1
  elif player1 == "S" and player2 == "P":
      print("Player 1's Scissors cuts Paper and wins!")
      print()
      player1Score += 1
  elif player1 == "S" and player2 == "S":
      print("It's a tie!")
      print()

  print("Player 1 has", player1Score, "wins.")
  print("Player 2 has", player2Score, "wins.")

  if player1Score == 3 or player2Score == 3:
    print("Thanks for playing!")
    exit()
  else:
    continue
 
 
