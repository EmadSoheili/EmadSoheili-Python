import random

print ("Hi, Let's Start \n"
       "Type Rock for Rock\n"
       "Type Paper for Paper\n"
       "Type Scissors for Scissors\n"
       "Type Quit for Quit\n"
       )

choices = ("rock", "paper", "scissors")

while True:
       wins = input("Enter the ultimate number of wins: \n")
       if not wins.isdigit():
              continue
       else:
              wins = int(wins)
              break


compWins = 0
myWins = 0

while True:
       myChoice = input("Rock, Paper, or Scissors? ").lower()
       compChoice = random.choice(choices)

       if myChoice == "Quit":
              break

       if myChoice == compChoice:
              print("It is a tie! Try again please.","\n")
              continue

       elif myChoice == "rock":
              if compChoice == "scissors":
                     print(f'{myChoice} beats {compChoice}.You win!')
                     myWins += 1
                     print("Your wins:", myWins)
                     print("Computer wins: ", compWins,"\n")

              elif compChoice == "paper":
                     print(f'{compChoice} beats {myChoice}.Computer wins!')
                     compWins += 1
                     print("Your wins:", myWins)
                     print("Computer wins: ", compWins,"\n")

       elif myChoice == "paper":
              if compChoice == "rock":
                     print(f'{myChoice} beats {compChoice}.You win!')
                     myWins += 1
                     print("Your wins:", myWins)
                     print("Computer wins: ", compWins,"\n")

              elif compChoice == "scissors":
                     print(f'{compChoice} beats {myChoice}.Computer wins!')
                     compWins += 1
                     print("Your wins:", myWins)
                     print("Computer wins: ", compWins,"\n")

       elif myChoice == "scissors":
              if compChoice == "paper":
                     print(f'{myChoice} beats {compChoice}.You win!')
                     myWins += 1
                     print("Your wins:", myWins)
                     print("Computer wins: ", compWins,"\n")

              elif compChoice == "rock":
                     print(f'{compChoice} beats {myChoice}.Computer wins!')
                     compWins += 1
                     print("Your wins:", myWins)
                     print("Computer wins: ", compWins,"\n")
       else:
              continue

       if (compWins == wins) or (myWins == wins):
              playAgain = input("Do you want to play again? Yes or No? ").lower()
              if playAgain == "yes":
                     myWins = 0
                     compWins = 0
              else:
                     break
