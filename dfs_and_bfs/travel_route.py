# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

# tickets = [["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"], ["AAA", "ICN"]] 의 경우 모든 티켓을 사용할 수 없음
def wrong(tickets):
    answer = []

    current = "ICN"
    answer.append("ICN")

    while tickets:
        candidate = []
        
        for ticket in tickets:
            if ticket[0] == current:
                candidate.append(ticket)
        
        candidate.sort(key=lambda x:x[1])
        answer.append(candidate[0][1])
        current = candidate[0][1]
        tickets.remove(candidate[0])
                
    print(tickets)
    return answer

from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
    
    for start in graph:
        graph[start].sort(reverse=True)
    
    route = []
    
    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        route.append(node)
    
    dfs("ICN")
    return route[::-1]

