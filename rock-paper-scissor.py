import random
        
game = {"r" : "rock", "p" : "paper", "s" : "scissors"}
keys = list(game.keys())
values = list(game.values())
number_games = int(input("the winner is decided after how many games: "))
x = 1
count_p1 = 0
count_p2 = 0
while x <= number_games:
    player_one = random.choice(values)
    print(f"player p1 selects {player_one}")
    player_two = random.choice(values)
    print(f"player p2 selects {player_two}")
    if player_one == player_two:
        print(f"Game {x}. Tie, Play again")
        x = x + 1
    elif (player_one == "r" and player_two == "s") or (player_one == "s" and player_two == "p") or (player_one == "p" and player_two == "r"):
        print(f"Game {x}, player one won")
        count_p1 = count_p1 + 1
        x = x + 1
    else:
        print(f"Game {x}, player two won")
        count_p2 = count_p2 + 1
        x = x + 1
     
if count_p1 > count_p2:
    print(f"In {number_games} the winner is player . p1 wins {count_p1} times")
else:
    print(f"In {number_games} the winner is p2. p2 {count_p2} times")


