import sys

def hand_probability():
    hand_names = ['nothing','one pair','two pairs','three of a kind',
                  'a straight','a flush','a full house','four of a kind',
                  'a straight flush','a royal flush']
    hands = [0]*10
    total = 0
    for line in sys.stdin:
        total += 1
        hand_rank = int(line[-2:-1])
        hands[hand_rank] += 1

    for i in range(10):
        print("The probability of {} is {:.4f}%".format(hand_names[i],hands[i]*100/total))

if __name__ == '__main__':
    hand_probability()
