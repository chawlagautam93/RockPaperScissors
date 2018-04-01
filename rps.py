import random

i = ["r", "p", "s"]

comp = random.choice(i)

player = input("r, p, s?")

print("Player: ", player)
print("Computer: ", comp)

if comp == player:
  print("Tie")
else:
  if player ==  "r":
    print(("You Win", "You Lose")[comp =="p"])
  elif player == "p":
    print(("You Win", "You Lose")[comp =="s"])
  elif player == "s":
