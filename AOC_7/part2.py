from functools import cmp_to_key

scoring_order = list("AKQT98765432J")

def get_game_type(game):
    buckets = [0 for i in scoring_order]
    jokers = 0
    for card in game:
        if card == "J":
            jokers += 1
            continue
        
        buckets[scoring_order.index(card)] += 1

    # Sort buckets
    buckets.sort(reverse=True)

    # Now handle jokers - a joker has the effect of doing whatever is necessary to
    # make the best hand possible.

    buckets[0] += jokers

    if buckets[0] == 5:
        return 10
    if buckets[0] == 4 and buckets[1] == 1:
        return 9
    if buckets[0] == 3 and buckets[1] == 2:
        return 8
    if buckets[0] == 3 and buckets[1] == 1:
        return 7
    if buckets[0] == 2 and buckets[1] == 2:
        return 6
    if buckets[0] == 2 and buckets[1] == 1:
        return 5
    if buckets[0] == 1:
        return 1
    
    print("FAILED TO CATEGORISE: " + str(game))
    import sys; sys.exit()

game_type_lookup = {
    10: "Five of a kind",
    9: "Four of a kind",
    8: "Full house",
    7: "Three of a kind",
    6: "Two pair",
    5: "One pair",
    1: "High card"
}

def evaluate_games(first, second):
    first = first[0]
    second = second[0]

    first_type = get_game_type(first)
    second_type = get_game_type(second)

    if first_type > second_type:
        return 1
    elif first_type < second_type:
        return -1
    else:
        for i in range(5):
            if scoring_order.index(first[i]) > scoring_order.index(second[i]):
                return -1
            elif scoring_order.index(first[i]) < scoring_order.index(second[i]):
                return 1
            
    return 0

with open("input.txt") as f:
    games = f.read().split("\n")

    parsed = []

    for game in games:
        cards = game.split(" ")[0]
        score = game.split(" ")[1]

        print("Evaluated " + cards + " to be type " + str(get_game_type(cards)))

        parsed.append((cards, score))

    parsed.sort(key=cmp_to_key(evaluate_games))

    total = 0
    i = 0
    for game in parsed:
        total += int(game[1]) * (i + 1)
        i += 1

    print(total)