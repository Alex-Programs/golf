with open("input.txt") as f:
    lines = f.read().split("\n")

    times = [56, 97, 78, 75]
    distances = [546, 1927, 1131, 1139]
    times = [int("".join([str(x) for x in times]))]
    distances = [int("".join([str(x) for x in distances]))]
    print(times, distances)
    #times = [71530]
    #distances = [940200]

    #times = [7, 15, 30]
    #distances = [9, 40, 200]

    for (i, time) in enumerate(times):
        distance_record = distances[i]
        c = 0
        for x in range(0, time):
            speed = x
            travelled = speed * (time - x)
            if travelled > distance_record:
                c += 1

        print(c)