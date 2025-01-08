import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

rolled = roll()



while True:
    players = input("How many players are there? (2-4): " )
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:  print("Must be bewteen 2-4")

    else: print("Enter a number")

print("Number of players =", players)


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer", player_index + 1, "has started!\n")
        print("Your total score is", player_scores[player_index])
        current_score = 0
        
        while True:
            player_roll = input("Would you like to role? (y) :" )
            if player_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1, Turn finished!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value, "!")
                
            print("Your current score is", current_score, "!")
       
        player_scores[player_index] += current_score
        print("Your total score is", player_scores[player_index])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)



       


       
        
        
            
    

        
















    

