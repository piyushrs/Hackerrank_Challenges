def factorial(n):
    f = [1]
    for i in range(1, n+1):
        f.append(i*f[i-1])
    return f[n]

print(factorial(5))