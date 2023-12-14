def evaluate_if_valid(part, contigs):
    # We have a part of dots and hashes, and a list of the contiguous lengths of the hashes
    # We need to check that the part matches up to the contigs
    # Return True if it does, False if it doesn't
    contig_section_length = 0
    contig_sections = []
    for i in range(len(part)):
        if part[i] == "#":
            contig_section_length += 1
        else:
            if contig_section_length != 0:
                contig_sections.append(contig_section_length)
                contig_section_length = 0

    if contig_section_length != 0:
        contig_sections.append(contig_section_length)

    #print(contig_sections, contigs)

    if contig_sections == contigs:
        return True
    else:
        return False

def make_all_possibilities(parts):
    # Produce all permutations of ? parts (# or .)
    # Return a list of all possibilities
    to_randomise_indexes = []
    for i in range(len(parts)):
        if parts[i] == "?":
            to_randomise_indexes.append(i)

    upper_bound = 2 ** len(to_randomise_indexes)
    possibilities = []
    for i in range(upper_bound):
        binary = bin(i)[2:].zfill(len(to_randomise_indexes))
        possibility = list(parts)
        for j in range(len(binary)):
            possibility[to_randomise_indexes[j]] = "#" if binary[j] == "1" else "."
        possibilities.append("".join(possibility))

    return possibilities

with open("input.txt") as f:
    lines = f.read().split("\n")\
    
    total_valid = 0
    for line in lines:
        parts, contig = line.split(" ")
        parsed = list(parts)
        out = []
        for i in range(5):
            print(i)
            out += parsed
            out.append("?")

        parts = out

        parts = list(parts)
        contig = contig.split(",")
        contig = [int(x) for x in contig]

        out = []
        for i in range(5):
            out += parts

        parts = out

        print(parts)
        poss = make_all_possibilities(parts)
        #print(poss)
        valid_count = 0
        for p in poss:
            if evaluate_if_valid(p, contig):
                valid_count += 1

        print(valid_count)
        total_valid += valid_count

    print(total_valid)