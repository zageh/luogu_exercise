s = input().strip()
l = len(s)

cnt = 0
for x in s:
    if x == 'W':
        cnt += 1
        
print ("West" if 2 * cnt > l else "East")