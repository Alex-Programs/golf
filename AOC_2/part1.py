with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    s = 0

    for line in lines:
        game_id = int(line.split(" ")[1].replace(":", ""))
        line = line.replace(",", ";")
        line = line.replace(":", ";")
        sections = line.split(";")
        comes_out = sections[1:]
        
        reds = 0
        greens = 0
        blues = 0

        for section in comes_out:
            section = section.strip()
            if "red" in section:
                r = int(section.split(" ")[0])
                if r > reds:
                    reds = r
            elif "green" in section:
                g = int(section.split(" ")[0])
                if g > greens:
                    greens = g
            elif "blue" in section:
                b = int(section.split(" ")[0])
                if b > blues:
                    blues = b

        print(game_id, reds, greens, blues)

        power = reds * greens * blues

        print(power)

        s += power

    print(s)