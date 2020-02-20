n,m,d = map(int, input().split())

grid = []

buf = {}

for j in range(n):
    grid.append(list(map(int, input().split())))
    for k in range(len(grid[j])):
        buf[grid[j][k]] = (j,k)
q = int(input())
al = []

cost = [0] * ((n*m)+1)

for i in range(d+1,n*m+1):
    cost[i] = cost[i-d] + abs(buf[i-d][0] - buf[i][0]) + abs(buf[i-d][1] - buf[i][1])

for _ in range(q):
    l,r = map(int, input().split())
    al.append([l,r])
    

for l,r in al:
    print(cost[r]-cost[l])
            
                
