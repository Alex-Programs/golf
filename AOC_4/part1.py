with open("input.txt") as f:
    lines = f.read().split("\n")

    s = 0
    for line in lines:
        sec_a = line.split("|")[0].split(":")[1].strip().replace("  ", " ")
        print(sec_a.split(" "))
        sec_b = line.split("|")[1].strip().replace("  ", " ")
        print(sec_b.split(" "))

        nums_a = [int(x) for x in sec_a.split(" ")]
        nums_b = [int(x) for x in sec_b.split(" ")]

        nums_a = set(nums_a)
        nums_b = set(nums_b)

        overlap = nums_a.intersection(nums_b)
        amount = len(overlap)

        if amount > 0:
            s += 2 ** (amount - 1)

    print(s)