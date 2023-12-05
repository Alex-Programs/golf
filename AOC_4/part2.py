with open("input.txt") as f:
    lines = f.read().split("\n")

    lines2 = [0 for x in lines]

    i = 0
    for line in lines:
        sec_a = line.split("|")[0].split(":")[1].strip().replace("  ", " ")
        sec_b = line.split("|")[1].strip().replace("  ", " ")

        nums_a = [int(x) for x in sec_a.split(" ")]
        nums_b = [int(x) for x in sec_b.split(" ")]

        nums_a = set(nums_a)
        nums_b = set(nums_b)

        overlap = nums_a.intersection(nums_b)
        amount = len(overlap)

        lines2[i] += 1

        if amount > 0:
            for a in range(i+1, i+amount+1):
                lines2[a] += (lines2[i])

        print(lines2)

        i += 1

    print(sum(lines2))