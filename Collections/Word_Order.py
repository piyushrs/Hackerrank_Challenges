from collections import Counter

l = []
n = int(input())
for _ in range(n):
    l.append(input())

c = Counter(l)
print(len(c))
for i in c.values():
    print(i, end = " ")