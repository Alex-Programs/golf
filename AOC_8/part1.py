from dataclasses import dataclass

@dataclass
class Element:
    text: str
    left: str
    right: str
    index_left: int
    index_right: int

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

    i = 0
    current_index = AAA_position
    while True:
        current_string = nodes[current_index].text
        if current_string == "ZZZ":
            print(i)
            break

        print(current_index, current_string)

        instruction = instructions[i % len(instructions)]
        if instruction == "L":
            current_index = nodes[current_index].index_left
        elif instruction == "R":
            current_index = nodes[current_index].index_right
        else:
            print("ERROR")
            break

        i += 1