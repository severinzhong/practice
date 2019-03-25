def findMinStep(board , hand) :
    def status(board , idx , ball) :
        board = board[:idx]+ ball + board[idx:]
        i = 0
        while i <len(board)-2 :
            if board[i] == board[i+1] and board[i+2] == board[i+1] :
                j = i + 2
                while j<len(board) and board[j]==board[i] :
                    j += 1
                board = board[:i] + board[j:]
                i = 0
            else :
                i += 1
        return board
    def search(board , hand, n) :
        #print(board , hand)
        if board == '' :
            return n
        if hand == '' :
            return -1 
        ret = 1<<32
        for i in range(len(board)) :
            for j in range(len(hand)) :
                t = search(status(board,i,hand[j]) , hand[:j]+hand[j+1:] , n+1)
                if t>0 and ret>t :
                    ret = t 
        if ret<(1<<32) :
            return ret
        else :
            return -1
    import collections
    def dfs(s, c):
        if not s: return 0
        res, i = float("inf"), 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]: j += 1
            incr = 3 - (j - i)
            if c[s[i]] >= incr:
                incr = 0 if incr < 0 else incr
                c[s[i]] -= incr
                tep = dfs(s[:i] + s[j:], c)
                if tep >= 0: res = min(res, tep + incr)
                c[s[i]] += incr
            i = j
        return res if res != float("inf") else -1
    return dfs(board, collections.Counter(hand))


if __name__ == '__main__' :
    print(findMinStep("WWRRBBWW","WRBRW"))