def dijkstra(n , idx , edges) :
    '''
        deges = dict()
        edges[(i,j)] = d
    '''
    cost = [1<<32 for _ in range(n)]
    visit = [False for _ in range(n)]
    def findshortest(cost) :
        ret = 1<<32
        retid = 0
        for i in range(n) :
            if cost[i]<ret and not visit[i]:
                ret = cost[i]
                retid = i
        return retid
    cost[idx] = 0
    visit[idx] = True 
    for i in edges[idx]:
        cost[i] = edges[idx][i]
    node = findshortest(cost)
    while node :
        for i in edges[node] : #update cost
            newcost = cost[node] + edges[node][i]
            if newcost<cost[i] :
                cost[i] = newcost
        visit[node] = True
        node = findshortest(cost)
    return cost
if __name__ == "__main__":
    n = 4
    edges = [dict() for _ in range(n)]
    edge = [[0,1],[1,2],[2,3],[1,3]]
    d = [1,2,3,1]
    for i in range(len(d)) :
        edges[edge[i][0]][edge[i][1]] = d[i]
        edges[edge[i][1]][edge[i][0]] = d[i]
    print(dijkstra(n , 0 , edges))