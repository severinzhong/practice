class Solution:
    def findMinHeightTrees(self, n, edges) :  #TLE
        edge = [set() for _ in range(n)]
        node = [False for _ in range(n)]
        ret = n+1
        for i in edges :
            edge[i[0]].add(i[1])
            edge[i[1]].add(i[0])
        def dfs(i) :
            ans = 0
            for j in edge[i] :
                if not node[j] :
                    node[j] = True
                    ans = max(ans , dfs(j)+1)
            return ans
        retset = []
        for i in range(n) :
            node = [False for _ in range(n)]
            node[i] = True
            ans = dfs(i)
            if ans<ret :
                ret = ans 
                retset = [i]
            elif ans == ret :
                retset.append(i)
        return retset
    def findMinHeightTrees2(self,n,edges) : #LTE
        step = [[1<<32 for _ in range(n) ]for _ in range(n)]
        for i in range(n) :
            step[i][i] = 0
        for i in edges :
            step[i[0]][i[1]] = 1
            step[i[1]][i[0]] = 1
        for i in range(n) :
            for j in range(n) :
                for k in range(n) :
                    if i!=j and j!=k and k!=i :
                        if step[i][k]+step[k][j]<step[i][j] :
                            step[i][j] = step[i][k]+step[k][j] 
        ret = 1<<32
        retset = []
        for i in range(n) :
            ans = max(step[i])
            if ret>ans :
                ret = ans
                retset = []
            if ret == ans :
                retset.append(i)
        return retset
    def findMinHeightTrees3(self,n,edges):
        if not n: return []
        e = [[] for _ in range(n)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)

        def longest_path(u, par=None):
            mx = []
            for v in e[u]:
                if v != par:
                    now = longest_path(v, u)
                    if len(now) > len(mx):
                        mx = now
            mx.append(u)
            return mx
        fr = longest_path(0)[0]
        path = longest_path(fr)
        k = len(path)
        return path[(k-1)>>1 : (k+2)>>1]
if __name__ == "__main__":
    n = 189
    edges = [[0,1],[0,2],[2,3],[1,4],[4,5],[3,6],[2,7],[5,8],[6,9],[5,10],[10,11],[5,12],[1,13],[9,14],[5,15],[2,16],[4,17],[15,18],[16,19],[10,20],[4,21],[12,22],[0,23],[8,24],[17,25],[10,26],[5,27],[12,28],[16,29],[20,30],[2,31],[26,32],[4,33],[33,34],[14,35],[23,36],[8,37],[25,38],[10,39],[23,40],[3,41],[16,42],[34,43],[26,44],[33,45],[33,46],[38,47],[41,48],[38,49],[42,50],[24,51],[20,52],[35,53],[13,54],[18,55],[45,56],[31,57],[29,58],[12,59],[48,60],[34,61],[29,62],[37,63],[17,64],[36,65],[0,66],[51,67],[49,68],[63,69],[35,70],[15,71],[34,72],[7,73],[16,74],[65,75],[50,76],[70,77],[5,78],[51,79],[47,80],[51,81],[32,82],[75,83],[66,84],[53,85],[84,86],[11,87],[70,88],[69,89],[71,90],[90,91],[29,92],[14,93],[58,94],[24,95],[12,96],[46,97],[63,98],[18,99],[29,100],[57,101],[30,102],[39,103],[99,104],[61,105],[58,106],[101,107],[37,108],[71,109],[44,110],[81,111],[85,112],[76,113],[32,114],[78,115],[49,116],[79,117],[55,118],[64,119],[105,120],[91,121],[54,122],[49,123],[83,124],[10,125],[42,126],[74,127],[120,128],[107,129],[40,130],[24,131],[47,132],[75,133],[29,134],[119,135],[24,136],[60,137],[52,138],[117,139],[124,140],[138,141],[88,142],[8,143],[143,144],[93,145],[62,146],[101,147],[40,148],[92,149],[81,150],[60,151],[144,152],[56,153],[99,154],[53,155],[107,156],[63,157],[119,158],[12,159],[0,160],[8,161],[137,162],[98,163],[36,164],[154,165],[79,166],[158,167],[59,168],[18,169],[28,170],[38,171],[157,172],[74,173],[62,174],[149,175],[48,176],[4,177],[122,178],[101,179],[147,180],[100,181],[105,182],[124,183],[120,184],[74,185],[97,186],[90,187],[16,188]]
    #print(Solution().findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(Solution().findMinHeightTrees3(n,edges))