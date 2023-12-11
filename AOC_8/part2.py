from dataclasses import dataclass

@dataclass
class Element:
    text: str
    left: str
    right: str
    index_left: int
    index_right: int

@dataclass
class Path:
    start_index: 0
    current_index: 0
    steps: 0

with open("input.txt") as f:
    lines = f.read().split("\n")

    nodes = []

    instructions = lines[0]

    AAA_position = 0

    for line in lines[2:]:
        text, others = line.split(" = ")
        left, right = others.strip().replace("(", "").replace(")", "").split(", ")
        print(text, left, right)
        nodes.append(Element(text, left, right, 0, 0))

        if text == "AAA":
            AAA_position = len(nodes) - 1

    for node in nodes:
        ind_l = 0
        ind_r = 0
        for i, n in enumerate(nodes):
            if n.text == node.left:
                ind_l = i
            if n.text == node.right:
                ind_r = i

        node.index_left = ind_l
        node.index_right = ind_r

    print("".join([str(x) + "\n" for x in nodes]))

    #import sys; sys.exit()

    instruction_index = 0
    found_paths = []
    paths = []

    i = 0
    for node in nodes:
        if node.text.endswith("A"):
            paths.append(Path(i, i, 0))
        
        i += 1

    while True:
        adjusted_instruction_index = instruction_index % len(instructions)
        instruction = instructions[adjusted_instruction_index]

        print(paths)
        to_remove = []
        a = 0
        for path in paths:
            path.steps = path.steps + 1

            if instruction == "L":
                path.current_index = nodes[path.current_index].index_left
            elif instruction == "R":
                path.current_index = nodes[path.current_index].index_right

            print(path.current_index, nodes[path.current_index].text)

            if "XXX" in nodes[path.current_index].text:
                print("FOUND XXX ON PATH: " + str(path))
                import sys; sys.exit()

            if nodes[path.current_index].text.endswith("Z"):
                print("FOUND Z")
                found_paths.append(path.steps)
                to_remove.append(a)

            a += 1

        for i in to_remove:
            del paths[i]

        if len(paths) == 0:
            break

        instruction_index += 1

    import math
    print(math.lcm(*found_paths))