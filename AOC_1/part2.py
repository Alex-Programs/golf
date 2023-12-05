numbers = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]

with open("input.txt") as f:
    data = f.read().split("\n")
    s = 0
    for line in data:
        current_string = ""
        nums = []
        for char in line:
            if char.isdigit():
                nums.append(int(char))
                current_string = ""
            else:
                current_string += char
                for number in numbers:
                    if number[0] in current_string:
                        nums.append(number[1])
                        current_string = current_string[len(current_string) - len(number[0]):]

        #print(line + " | " + ";".join([str(x) for x in nums]))
        print(nums[0], nums[-1])

        s += int(str(nums[0]) + str(nums[-1]))

    print(s)