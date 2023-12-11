def predict_next(numbers):
    all_zeros = True
    for n in numbers:
        if n != 0:
            all_zeros = False
            break
    if all_zeros:
        return 0

    diffs = get_diffs(numbers)
    return numbers[-1] + predict_next(diffs)

def get_diffs(numbers):
    diffs = []
    for i in range(len(numbers) - 1):
        diffs.append(numbers[i + 1] - numbers[i])
    return diffs

with open("input.txt") as f:
    lines = f.read().split("\n")

    s = 0

    for line in lines:
        numbers = [int(x) for x in line.split(" ")]
        #numbers.reverse()

        print(numbers)
        print(predict_next(numbers))

        s += predict_next(numbers)

    print(s)