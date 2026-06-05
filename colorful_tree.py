import sys

data = sys.stdin.read().split()

note = [[0] * 22 for _ in range(1000005)]
time = [[0] * 22 for _ in range(1000005)]

n = int(data[0])
q = int(data[1])
idx = 2

out = []
for i in range(q):
    check = data[idx]
    
    if check == '1':
        x, y, z = [int(x) for x in data[idx + 1: idx + 4]]
        idx += 4
        
        while x and y >= 0:
            note[x][min(y, 21)] = z
            time[x][min(y, 21)] = i + 1
            
            x = x >> 1
            y -= 1
            
    else:
        x = int(data[idx + 1])
        idx += 2
        
        t = 0
        ans = 0
        length = 0
        
        while x and length <= 21:
            for j in range(length, 22):
                if time[x][j] > t:
                    t = time[x][j]
                    ans = note[x][j]
                    
            x >>= 1
            length += 1
            
        out.append(str(ans))
        
sys.stdout.write('\n'.join(out))