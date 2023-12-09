from dataclasses import dataclass

@dataclass
class lookup:
    from_range: (int, int)
    to_range: (int, int)

@dataclass
class Section:
    name: str
    maps: list[lookup]

def map_lookup(number, maps):
    for lookup in maps:
        print(f"Lookup {str(number)}: In range {lookup.to_range[0]}-{lookup.to_range[1]} {lookup.from_range[0]}-{lookup.from_range[1]}")
        if number >= lookup.from_range[0] and number < lookup.from_range[1]:
            number = lookup.to_range[0] + (number - lookup.from_range[0])
            print(f"Number is now {number}")
            break
    
    return number

def reverse_map_lookup(number, maps):
    for lookup in maps:
        #print(f"Lookup {str(number)}: In range {lookup.to_range[0]}-{lookup.to_range[1]} {lookup.from_range[0]}-{lookup.from_range[1]}")
        if number >= lookup.to_range[0] and number <= lookup.to_range[1]:
            number = lookup.from_range[0] + (number - lookup.to_range[0])
            #print(f"Number is now {number}")
            break
    
    return number

def check_if_num_in_seed_ranges(number, seed_pairs):
    for seed_pair in seed_pairs:
        if number >= seed_pair[0] and number <= seed_pair[0] + seed_pair[1]:
            return True
    
    return False

with open("input.txt") as f:
    sections = f.read().split("\n\n")
    
    seeds = sections[0].split("\n")[0].split(":")[1].strip().replace("  ", " ").replace("   ", " ").split(" ")
    seeds = [int(x) for x in seeds]
    seed_pairs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(seed_pairs)

    #import sys; sys.exit()

    maps = []

    for section in sections[1:]:
        name = section.split("\n")[0].split(":")[0].strip()
        print(name)
        
        maps_buff = []
        
        for line in section.split("\n")[1:]:
            if line == "":
                continue
            
            # eg 88 18 7
            nums = line.replace("   ", " ").replace("  ", " ").split(" ")
            nums = [int(x) for x in nums]
            print(nums)
            
            to_range = (nums[0], nums[0] + nums[2])
            from_range = (nums[1], nums[1] + nums[2])

            print(to_range)
            print(from_range)

            maps_buff.append(lookup(from_range, to_range))
        
        maps.append(Section(name, maps_buff))

    i = 0
    while True:
        seed = i
        #print("--")
        for m in reversed(maps):
            #print(seed)\\\
            seed = reverse_map_lookup(seed, m.maps)
        
        #print(seed)

        if check_if_num_in_seed_ranges(seed, seed_pairs):
            print(f"Found seed: {seed} corresponds to {i}")
            break

        i += 1

        if i % 100000 == 0:
            print(i)