x = list(map(int, input().split()))
p = input()
if eval(p.replace('x', str(x[0]))) == x[1]:
    print(True)
else:
    print(False)