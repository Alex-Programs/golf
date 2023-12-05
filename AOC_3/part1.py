from dataclasses import dataclass

@dataclass
class Symbol:
    position: tuple
    text: str

@dataclass
class PartNum:
    positions: list[tuple]
    number: int

def positions_adjacent(pos_a, pos_b):
    if pos_a[0] == pos_b[0] and pos_a[1] == pos_b[1]:
        return False
    
    if pos_a[0] == pos_b[0] and pos_a[1] == pos_b[1] + 1:
        return True
    
    if pos_a[0] == pos_b[0] and pos_a[1] == pos_b[1] - 1:
        return True
    
    if pos_a[0] == pos_b[0] + 1 and pos_a[1] == pos_b[1]:
        return True
    
    if pos_a[0] == pos_b[0] - 1 and pos_a[1] == pos_b[1]:
        return True
    
    if pos_a[0] == pos_b[0] + 1 and pos_a[1] == pos_b[1] + 1:
        return True
    
    if pos_a[0] == pos_b[0] + 1 and pos_a[1] == pos_b[1] - 1:
        return True
    
    if pos_a[0] == pos_b[0] - 1 and pos_a[1] == pos_b[1] + 1:
        return True
    
    if pos_a[0] == pos_b[0] - 1 and pos_a[1] == pos_b[1] - 1:
        return True
    
    return False


with open("input.txt") as f:
    lines = f.read().split("\n")

    symbols = []
    part_nums = []

    for line in lines:
        number_buff = []
        
        i = 0
        for char in line:
            if char.isdigit():
                number_buff.append((char, (i, lines.index(line))))
            else:
                if len(number_buff) > 0:
                    part_nums_poses = [x[1] for x in number_buff]
                    part_nums.append(PartNum(part_nums_poses, int("".join([x[0] for x in number_buff]))))
                    number_buff = []

                    if char != ".":
                        symbols.append(Symbol((i, lines.index(line)), char))
                else:
                    if char != ".":
                        symbols.append(Symbol((i, lines.index(line)), char))

            i += 1

        if len(number_buff) > 0:
            part_nums_poses = [x[1] for x in number_buff]
            part_nums.append(PartNum(part_nums_poses, int("".join([x[0] for x in number_buff]))))

    parts_sum = 0        
    
    for symbol in symbols:
        for part_num in part_nums:
            is_adjacent = False
            for pos in part_num.positions:
                if positions_adjacent(symbol.position, pos):
                    #print(symbol, part_num)
                    is_adjacent = True
                    break
            
            if is_adjacent:
                parts_sum += part_num.number

    print(parts_sum)

    # Part 2
    s = 0
    for symbol in symbols:
        if symbol.text == "*":
            adjacent_part_nums = []
            for part_num in part_nums:
                is_adjacent = False
                for pos in part_num.positions:
                    if positions_adjacent(symbol.position, pos):
                        is_adjacent = True
                        break
                
                if is_adjacent:
                    adjacent_part_nums.append(part_num)

            if len(adjacent_part_nums) == 2:
                s += adjacent_part_nums[0].number * adjacent_part_nums[1].number

    print(s)
