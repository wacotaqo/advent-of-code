import os
import sys

filename = "adventofcode2022_day02_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
rps_moves = fh.read().splitlines()
fh.close()

element_scores = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3  # Scissors
 }
 
round_scores_for_me = { # Just use the combinations
    ('A', 'X'): 3, # rock : rock => draw
    ('B', 'X'): 0, # paper : rock => lose
    ('C', 'X'): 6, # scissors : rock => win
    ('A', 'Y'): 6, # rock : paper => win
    ('B', 'Y'): 3, # paper : paper => draw
    ('C', 'Y'): 0, # scissors : paper => lose
    ('A', 'Z'): 0, # rock : scissors => lose
    ('B', 'Z'): 6, # paper : scissors => win
    ('C', 'Z'): 3, # scissors = scissors = draw
}

my_total_score = 0
my_round_score = 0
num_rounds = 0
for rps_move in rps_moves:
    (opp_move, my_move) = rps_move.split(' ')
    if my_move in element_scores: 
        my_element_score = element_scores[my_move]
    else: 
        my_element_score = 0
    if (opp_move, my_move) in round_scores_for_me:
        my_round_score = round_scores_for_me[(opp_move, my_move)]
    else:
        print("Cannot find move combination for (%s)!" % rps_move)
    
    num_rounds += 1
    print("%d = %d + %d" % (my_total_score, my_element_score, my_round_score))
    my_total_score = my_total_score + my_element_score + my_round_score
    
print("My total score: %d after %d rounds" % (my_total_score, num_rounds))

        
    

    
