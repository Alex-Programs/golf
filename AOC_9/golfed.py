def p(numbers):
    return numbers[-1] + p(d(numbers)) if any(numbers) else 0

def d(numbers):
    return [b-a for a, b in zip(numbers, numbers[1:])]
"""
with open("input.txt") as f:
    lines = f.read().split("\n")

    s = 0

    for line in lines:
        numbers = [int(x) for x in line.split(" ")]

        print(numbers)
        print(predict_next(numbers))

        s += predict_next(numbers)

    print(s)"""


data = open("input.txt").read().split("\n")
p = lambda x: x[-1] + p([b-a for a, b in zip(x, x[1:])]) if any(x) else 0
r = sum([
    int(p([int(l) for l in l.split(" ")])) for l in data
])

print(r)