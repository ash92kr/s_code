
def BFS():
    que=[]
    dr=(0, 0, 0, 1, -1)
    dc=(0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3,4), (1,2), (2,1)]
    que.append((sr, sc, sdir, 0))
    chk[sdir][sr][sc] =1
    while que:
        r, c, dir, cnt = que.pop(0)
        if r==er and c==ec and dir == edir : return cnt
        for i in range(1, 4):
            nr = r+ dr[dir]*i
            nc = c + dc[dir]*i
            if nr<0 or nr>=R or nc<0 or nc>=C : break
            if chk[dir][nr][nc] : continue
            if arr[nr][nc] ==1 : break
            que.append((nr, nc, dir, cnt+1))
            chk[dir][nr][nc]=1

        for i in range(2):
            ndir = turn[dir][i]
            if chk[ndir][r][c] : continue
            que.append((r,c,ndir, cnt+1))
            chk[ndir][r][c]=1



#main------------------------------------
R, C = map(int, input().split())
chk = [ [ [0]*C for i in range(R) ] for j in range(5) ]

arr = []
for i in range(R):
    arr.append(list(map(int, input().split())))
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr-=1; sc-=1
er-=1; ec-=1
sol=BFS()
print(sol)

