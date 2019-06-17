from scipy.sparse.csgraph import csgraph_from_dense,dijkstra

xs, ys, xt, yt = map(int, input().split())
n = int(input())

p = [(xs,ys,0),(xt,yt,0)]
for i in range(2,n+2):
    p.append(tuple(map(int,input().split())))
edge = [[-1]*(n+2)for i in range(n+2)]
 
for i in range(n+2):
    for j in range(i+1,n+2):
        edge[i][j] = edge[j][i] =  max(((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)**0.5 - p[i][2] - p[j][2],0.0)

#ここから
G = csgraph_from_dense(edge,null_value=-1)
print(dijkstra(G,indices=0)[1])