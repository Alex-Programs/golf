def lookup(lines, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return lines[y][x]
    except IndexError:
        return None

def find_connections(lines, x, y):
    # Connections are the places in adjacent squares where the pipes can be connected to the current square
    # S = Start, we don't know what this is... just pretend it connects to everything
    # | = Connects to N and S
    # - = Connects to E and W
    # L = Connects to N and E
    # J = Connects to N and W
    # 7 = Connects to S and W
    # F = Connects to S and E
    # . = Connects to nothing

    current_square = lookup(lines, x, y)
    current_square_directions = []
    if current_square == "S":
        current_square_directions = ["N", "E", "S", "W"]
    elif current_square == "|":
        current_square_directions = ["N", "S"]
    elif current_square == "-":
        current_square_directions = ["E", "W"]
    elif current_square == "↳":
        current_square_directions = ["N", "E"]
    elif current_square == "↲":
        current_square_directions = ["N", "W"]
    elif current_square == "↰":
        current_square_directions = ["S", "W"]
    elif current_square == "↱":
        current_square_directions = ["S", "E"]
    elif current_square == ".":
        return []
    
    output_connections = []
    for direction in current_square_directions:
        if direction == "N":
            if lookup(lines, x, y - 1) in ["|", "S", "↱", "↰",]:
                output_connections.append((x, y - 1))
        elif direction == "E":
            if lookup(lines, x + 1, y) in ["-", "S", "↰", "↲"]:
                output_connections.append((x + 1, y))
        elif direction == "S":
            if lookup(lines, x, y + 1) in ["|", "S", "↳", "↲"]:
                output_connections.append((x, y + 1))
        elif direction == "W":
            if lookup(lines, x - 1, y) in ["-", "S", "↱", "↳"]:
                output_connections.append((x - 1, y))

    return output_connections

with open("input.txt") as f:
    data = f.read().replace("L", "↳").replace("J", "↲").replace("7", "↰").replace("F", "↱")
    lines = data.split("\n")

    x_width = len(lines[0])
    y_width = len(lines)

    # Find S
    s_x = None
    s_y = None

    for y in range(y_width):
        for x in range(x_width):
            if lookup(lines, x, y) == "S":
                s_x = x
                s_y = y
                break

        if s_x != None:
            break

    print("Found S at (" + str(s_x) + ", " + str(s_y) + ")")

    distance = 0
    # Find points around s_x that link nicely
    connections = find_connections(lines, s_x, s_y)

    queue = []
    explored = []
    queue.append((s_x, s_y))

    while len(queue) > 0:
        current = queue.pop(0)
        explored.append(current)

        # Find connections
        connections = find_connections(lines, current[0], current[1])
        for connection in connections:
            if connection not in explored and connection not in queue:
                queue.append(connection)
                distance += 1

    print("Distance: " + str((distance+1) / 2))