
import heapq

def dijkstra(graph,start):
    dist={node:float('inf') for node in graph}
    dist[start]=0
    pq=[(0,start)]
    while pq:
        d,node=heapq.heappop(pq)
        for neigh,w in graph[node]:
            nd=d+w
            if nd<dist[neigh]:
                dist[neigh]=nd
                heapq.heappush(pq,(nd,neigh))
    return dist

if __name__=="__main__":
    g={
        'A':[('B',1),('C',4)],
        'B':[('C',2),('D',5)],
        'C':[('D',1)],
        'D':[]
    }
    print("Shortest paths from A:", dijkstra(g,'A'))
