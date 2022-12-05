import os
import sys

filename = "adventofcode2022_day02_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
rps_moves = fh.read().splitlines()
fh.close()

ROCK = 1
PAPER = 2
SCISSORS = 3

element_scores = {
    ROCK: 1, # Rock
    PAPER: 2, # Paper
    SCISSORS: 3  # Scissors
 }

strategy_guide_for_me = { # Just use the combinations
#X = lose
#Y = draw
#z = wind
    ('A', 'X'): SCISSORS, # rock : lose => scissors
    ('B', 'X'): ROCK, # paper : lose => rock
    ('C', 'X'): PAPER, # scissors : lose => paper
    ('A', 'Y'): ROCK, # rock : draw => rock
    ('B', 'Y'): PAPER, # paper : draw => paper
    ('C', 'Y'): SCISSORS, # scissors : draw => scissors
    ('A', 'Z'): PAPER, # rock : win => paper
    ('B', 'Z'): SCISSORS, # paper : win => scissors
    ('C', 'Z'): ROCK, # scissors = win = rock
}

round_scores_for_me = { # Just use the combinations
    ('A', ROCK): 3, # rock : rock => draw
    ('B', ROCK): 0, # paper : rock => lose
    ('C', ROCK): 6, # scissors : rock => win
    ('A', PAPER): 6, # rock : paper => win
    ('B', PAPER): 3, # paper : paper => draw
    ('C', PAPER): 0, # scissors : paper => lose
    ('A', SCISSORS): 0, # rock : scissors => lose
    ('B', SCISSORS): 6, # paper : scissors => win
    ('C', SCISSORS): 3, # scissors = scissors = draw
}

my_total_score = 0
my_round_score = 0
num_rounds = 0
for rps_move in rps_moves:
    (opp_move, result_needed) = rps_move.split(' ')
    if (opp_move, result_needed) in strategy_guide_for_me:
        my_move = strategy_guide_for_me[(opp_move, result_needed)]
    else:
        my_move = -1
        print("Cannot find move combination for (%s, %s)!" % (opp_move, result_needed))

    if my_move in element_scores: 
        my_element_score = element_scores[my_move]
    else: 
        my_element_score = 0
        print("Cannot find move for me(%s)!" % (my_move))
    
    if (opp_move, my_move) in round_scores_for_me:
        my_round_score = round_scores_for_me[(opp_move, my_move)]
    else:
        my_round_score = 0
        print("Cannot find move combination for (%s, %s)!" % (opp_move, my_move))

    num_rounds += 1
    print("%d = %d + %d" % (my_total_score, my_element_score, my_round_score))
    my_total_score = my_total_score + my_element_score + my_round_score
    
print("My total score: %d after %d rounds" % (my_total_score, num_rounds))

        
    

    
