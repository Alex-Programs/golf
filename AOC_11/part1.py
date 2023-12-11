def dist(a, b, empty_rows, empty_cols):
    simple_length = abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    for row in empty_rows:
        if a[0] < row < b[0] or b[0] < row < a[0]:
            simple_length += 1000000-1

    for col in empty_cols:
        if a[1] < col < b[1] or b[1] < col < a[1]:
            simple_length += 1000000-1

    return simple_length

with open("input.txt") as f:
    data = f.read().split("\n")
    data = [list(line) for line in data]

    empty_rows = []
    for i in range(len(data)):
        row = data[i]
        if row.count("#") == 0:
            empty_rows.append(i)

    print(empty_rows)

    empty_cols = []
    for col in range(len(data[0])):
        if [row[col] for row in data].count("#") == 0:
            empty_cols.append(col)

    print(empty_cols)

    galaxy_positions = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "#":
                galaxy_positions.append((row, col))

    s = 0
    i = 0

    for a in galaxy_positions:
        j = 0
        print(f"{i}/{len(galaxy_positions)}")
        for bo in range(i+1, len(galaxy_positions)):
            b = galaxy_positions[bo]

            j += 1

            distance = dist(a, b, empty_rows, empty_cols)

            #print(i, j, distance, a, b)

            s += distance

        i += 1

    print(s)