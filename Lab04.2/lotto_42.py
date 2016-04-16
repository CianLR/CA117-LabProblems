import sys
import random

SIMULATIONS = 1000000
lucky_nums = set([int(x) for x in sys.argv[1:]])
possible_nums = list(range(1,48))
matches = [0]*7

for _ in range(SIMULATIONS):
    sample = set(random.sample(possible_nums,6))
    matches[len(sample&lucky_nums)] += 1

for i in range(3,7):
    odds = SIMULATIONS//matches[i] if matches[i] > 0 else '?'
    print("Match {}'s : {:5d} ({} to 1)".format(i,matches[i],odds))
