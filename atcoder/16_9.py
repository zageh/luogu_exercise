x, y = map(int, input().split())

if x % 16 == 0 and y % 9 == 0 and x // 16 == y // 9:
    print("Yes")
else:
    print("No")