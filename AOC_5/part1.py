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

with open("input.txt") as f:
    sections = f.read().split("\n\n")
    
    seeds = sections[0].split("\n")[0].split(":")[1].strip().replace("  ", " ").replace("   ", " ").split(" ")
    seeds = [int(x) for x in seeds]
    print(seeds)

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

    location_lookup = maps[-1].maps

    for seed in seeds:
        # Cascade through every layer
        for section in maps:
            seed = map_lookup(seed, section.maps)
        print(seed)