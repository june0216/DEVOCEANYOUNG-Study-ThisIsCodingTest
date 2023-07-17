def solution(n, weak, dist):
    answer = 0
    
    # 방법 1. 취약지점 간의 거리를 구한다. -> 어려운데
    # 방법 2. O(n) 으로 돌면서 그리디하게 접근한다.
    
    dist = sorted(dist, reverse=True)
    
    term = []
    for i in range(len(weak)-1, 0, -1):
        term.append(weak[i]-weak[i-1])
    term.append(n-weak[-1]+weak[0])
    print(term)
        
        
    return answer
