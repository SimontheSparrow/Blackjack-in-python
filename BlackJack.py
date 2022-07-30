from random import random
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = [cards[random.randrange(
    0, len(cards)-1)], cards[random.randrange(0, len(cards)-1)]]
cpu_cards = [cards[random.randrange(
    0, len(cards)-1)], cards[random.randrange(0, len(cards)-1)]]
 
print(
    f"You have {player_cards[0]} and {player_cards[1]} \nCpu has {cpu_cards[0]} and one other")

choice = input("Do you want another card? ")

if choice.lower() == 'y' or choice.lower() == 'yes':
    player_cards.append(cards[random.randrange(0, len(cards)-1)])
    if cpu_cards[0] + cpu_cards[1] < 17:
        cpu_cards.append(cards[random.randrange(0, len(cards)-1)])

player_sum = 0
cpu_sum = 0

for card in player_cards:
    player_sum += card
for card in cpu_cards:
    cpu_sum += card


if len(player_cards) == 3 and len(cpu_cards) == 2:
    print(
        f"You have {player_cards[0]}, {player_cards[1]} and {player_cards[2]} \nCpu has {cpu_cards[0]} and {cpu_cards[1]}")
elif len(player_cards) == 3 and len(cpu_cards) == 3:
    print(
        f"You have {player_cards[0]}, {player_cards[1]} and {player_cards[2]} \nCpu has {cpu_cards[0]}, {cpu_cards[1]} and {cpu_cards[2]}")
elif len(player_cards) == 2 and len(cpu_cards) == 3:
    print(
        f"You have {player_cards[0]} and {player_cards[1]} \nCpu has {cpu_cards[0]}, {cpu_cards[1]} and {cpu_cards[2]}")
elif len(player_cards) == 2 and len(cpu_cards) == 2:
    print(
        f"You have {player_cards[0]} and {player_cards[1]} \nCpu has {cpu_cards[0]} and {cpu_cards[1]}")


if player_sum > 21:
    print("Bust!")
elif cpu_sum > 21 and player_sum < 21:
    print("You win!")
elif player_sum > cpu_sum:
    print("You win!")
elif player_sum < cpu_sum:
    print("You lose!")
