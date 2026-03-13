
def bellman_ford(vertices,edges,start):
    dist=[float('inf')]*vertices
    dist[start]=0
    for _ in range(vertices-1):
        for u,v,w in edges:
            if dist[u]!=float('inf') and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
    return dist

if __name__=="__main__":
    v=5
    edges=[
        (0,1,-1),
        (0,2,4),
        (1,2,3),
        (1,3,2),
        (1,4,2),
        (3,2,5),
        (3,1,1),
        (4,3,-3)
    ]
    print("Distances from 0:", bellman_ford(v,edges,0))
