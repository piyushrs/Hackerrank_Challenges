# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    x = list(map(int, input().split()))
    subs = []
    for i in range(x[1]):
        subs.append(list(map(float, input().split())))
    
    students = list(zip(*subs))
    for i in students:
        print(sum(i)/len(i))