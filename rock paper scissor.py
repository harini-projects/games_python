import random

def get_choices():
  player_choice=input("Enter your choice:")
  options=["rock","paper","scissors"]
  computer_choice=random.choice(options)
  choice={"player":player_choice,"computer":computer_choice}

  return choice



def check_win(player,computer):
  print(f"you choose {player} , computer choose {computer}")
  if player==computer:
    print("It is a tie!")
  elif player=="rock":
    if computer=="paper":
      print("paper crushes the rock, You lose")
    else:
      print("rock smashes the scissors, You Win")
      
  elif player=="paper":
    if computer=="scissors":
      print("scissor cuts the paper, You Win")
    else:
      print("paper crushes the rock, You lose")
      
  elif player=="scissors":
    if computer=="paper":
      print("scissor cuts the paper, You Win")
    else:
      print("rock smashes the scissor, You lose")
          
  
choice=get_choices()
result=check_win(choice["player"],choice["computer"])