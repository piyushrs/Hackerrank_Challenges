def merge_the_tools(string, k):
    l = list(string)
    u = []
    while l:
        u.append(l[:k])
        del l[:k]
    
    for i in u:
        a = ""
        for j in i:
            if j not in a:
                a += j
        print(a)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)