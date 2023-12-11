class CL:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    lines = [list(line) for line in lines]

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

    S_VALUE = "|"#"↱"
    lines[s_y][s_x] = S_VALUE

    distance = 0
    # Find points around s_x that link nicely
    connections = find_connections(lines, s_x, s_y)

    queue = []
    explored = []
    queue.append((s_x, s_y))
    loop_positions = [(s_x, s_y)]

    while len(queue) > 0:
        current = queue.pop(0)
        explored.append(current)

        # Find connections
        connections = find_connections(lines, current[0], current[1])
        for connection in connections:
            if connection not in explored and connection not in queue:
                queue.append(connection)
                if connection not in loop_positions:
                    loop_positions.append(connection)
                distance += 1

    # Just visualise the loop, while also creating a loop-only geometry
    looplines = []
    for y in range(y_width):
        line = []
        for x in range(x_width):
            if (x, y) in loop_positions:
                lookedup = lookup(lines, x, y)
                print(lookedup, end="")
                line.append(lookedup)
            else:
                print(".", end="")
                line.append(".")
        print()
        looplines.append(line)

    print("\n\n")

    # Strategy for finding what's inside the loop:
    # Go left->right for each line
    # If amount of vertical pipes (that are in loop data) is odd, then it's enclosed
    # If amount of vertical pipes (that are in loop data) is even, then it's not enclosed
    # Consider a ↱↲ to be a vertical pipe, INCLUDING WITH ARBITRARY AMOUNTS OF - IN BETWEEN
    # Consider a ↳↰ to be a vertical pipe, INCLUDING WITH ARBITRARY AMOUNTS OF - IN BETWEEN
        
    interior_coordinates = []
    for y in range(y_width):
        override_x = None
        verticals_count = 0
        for x in range(x_width):
            character = looplines[y][x]
            if y == 5:
                print(character + str(override_x))

            if override_x and x < override_x:
                print("Skipping")
                continue

            if character == "|":
                verticals_count += 1
                continue

            is_vertical_pair = False
            if character == "↱":
                # Keep going until you find a ↲ or something other than -
                for x2 in range(x+1, x_width):
                    if looplines[y][x2] == "↲":
                        is_vertical_pair = True
                        print("Found a ↱↲ pair")
                        override_x = x2
                        break
                    elif looplines[y][x2] != "-":
                        # Found something other than a ↲ or -, so this is not an enclosed space
                        is_vertical_pair = False
                        break

            if character == "↳":
                # Keep going until you find a ↰ or something other than -
                for x2 in range(x+1, x_width):
                    if looplines[y][x2] == "↰":
                        is_vertical_pair = True
                        print("Found a ↳↰ pair")
                        override_x = x2
                        break
                    elif looplines[y][x2] != "-":
                        # Found something other than a ↰ or -, so this is not an enclosed space
                        is_vertical_pair = False
                        break

            if is_vertical_pair:
                verticals_count += 1
                continue

            if verticals_count % 2 == 1:
                interior_coordinates.append((x, y))

    print(interior_coordinates)
    print(len(interior_coordinates))

    # Visualise the interior coordinates alongside the loop
    out = 0
    for y in range(y_width):
        for x in range(x_width):
            if (x, y) in loop_positions and interior_coordinates:
                print(CL.WARNING + "■", end="")
                continue

            if (x, y) in loop_positions:
                lookedup = lookup(lines, x, y)
                print(lookedup, end="")

            if (x, y) in interior_coordinates:
                out += 1
                print("O", end="")

            if (x, y) not in loop_positions and (x, y) not in interior_coordinates:
                print(".", end="")
        print()

    print(out)