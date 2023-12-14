with open("input.txt") as f:
    data = f.read().split("\n")
    data = [list(line) for line in data]

    for line in data:
        print("".join(line))

    # Go through backwards moving upwards if possible
    for o in range(len(data)):
        i = 0
        for line in data:
            j = 0
            for char in line:
                if char == "O":
                    if i != 0:
                        # Check if we can go up
                        #print(data[i - 1][j])
                        if data[i - 1][j] == ".":
                            data[i - 1][j] = "O"
                            data[i][j] = "."
                
                j += 1

            i += 1

    # Visualise
    print("\n")
    for line in data:
        print("".join(line))

    # Score
    i = 0
    score = 0
    for line in data:
        point_worth = len(data) - i
        count_os = line.count("O")
        score += count_os * point_worth

        i += 1

    print(score)