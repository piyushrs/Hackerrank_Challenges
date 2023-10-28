s = "BANANA"
stuart = 0
kevin = 0
for i in range(len(s)):
    if s[i] in "AEIOU":
        kevin += len(s) - i
        print(f"Kevin {kevin}")
    else:
        stuart += len(s) - i
        print(f"Stuart {stuart}")

if kevin>stuart:
    print(f"Kevin {kevin}")
elif stuart > kevin:
    print(f"Stuart {stuart}")
else:
    print("Draw")