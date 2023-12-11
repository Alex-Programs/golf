p=lambda x:x[-1]+p([b-a for a,b in zip(x,x[1:])])if any(x)else 0
print(sum([int(p([int(l) for l in l.split()]))for l in open(0).read().split("\n")]))