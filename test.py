
total = 0
l = [1,2,3,4,5]
l.sort(reverse=True)
while len(l) >= 3:
    print(l)
    total += 1
    print(total)
    l = l[3:]
    print(l)
else:
    total += sum(l)

print(total)