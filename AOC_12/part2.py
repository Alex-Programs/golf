def go_left_right_getting_possibilities(parts, contig):
    # Generate permutations left->right modulating question marks, abandoning a branch if it's invalid against contig
    # Essentially, do a breadth-first-search of the search space, only going along branches that have worth
    # Return the amount of valid permutations.

    # Make BFS queue
    count = 0
    queue = []
    while len(queue) > 0:
        element = queue.pop(0)
        element_index = len(element)
        # Check for 

with open("input.txt") as f:
    lines = f.read().split("\n")\
    
    total_valid = 0
    for line in lines:
        parts, contig = line.split(" ")
        parsed = list(parts)
        out = []
        for i in range(5):
            print(i)
            out += parsed
            out.append("?")

        parts = out

        parts = list(parts)
        contig = contig.split(",")
        contig = [int(x) for x in contig]

        out = []
        for i in range(5):
            out += parts

        parts = out

        print(parts)

        print(valid_count)
        total_valid += valid_count

    print(total_valid)