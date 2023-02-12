           #Dice Game#
import random
game=[1,2,3,4,5,6]
computer=random.choice(game)
player=input("select a number between 1-6\nPlayer:")
print("computer:",computer)
if "computer">"player":
  print("computer won")
elif "player">"computer":
  print("player won")
else:
    print("TIE")