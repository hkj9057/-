import collections

count = 0
a, b = map(int, input().split())
matrix = []
for i in range(b):
    temp = list(map(int, input().split()))
    matrix.append(temp)
print(matrix)

queue = collections.deque()

for x in range(b):
    for y in range(a):
        if(matrix[x][y] == 1):
            queue.append((x,y))
# 0,0 0,1(100) 0,2(100)
# 1,0 1,1 1,2(100)
# 2,0 2,1 2,2(1)
arrow = [(-1,0),(1,0),(0,-1),(0,1)]
while(len(queue) != 0):

    x, y, count = queue.popleft()

    for t_x, t_y in arrow:
        c_x = x + t_x
        c_y = y + t_y

    #조건
    if(c_x < x and c_x >= 0 and c_y < y and c_y >= 0):
        if(matrix[c_x][c_y] != -1 and matrix[c_x][c_y] == 0):
            matrix[c_x][c_y] = 100
            queue.append((c_x, c_y,count + 1))
flag = 0
for x in range(b):
    for y in range(a):
        if(matrix[x][y] == 0):
            flag = 1
            break
if(flag == 1):
    print(-1)
else:
    print(count)
