import heapq  # 우선순위 큐 (작은 값 먼저 뽑기 위함)
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # 그래프 만들기 (각 노드가 연결된 노드, 시간 저장)
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))  # 양방향이니까 반대도 추가!

        # 거리와 경로 수를 저장할 배열
        dist = [float('inf')] * n  # 처음에는 모두 무한대 거리
        ways = [0] * n             # 경로 수 0으로 초기화

        dist[0] = 0   # 0번은 시작점이니까 거리 0
        ways[0] = 1   # 자기 자신까지 오는 건 1가지 방법

        # 다익스트라를 위한 우선순위 큐
        heap = [(0, 0)]  # (시간, 노드번호)

        while heap:
            time_so_far, node = heapq.heappop(heap)

            # 이미 더 빠른 길이 있으면 무시
            if time_so_far > dist[node]:
                continue

            # 이웃 노드들 보기
            for next_node, travel_time in graph[node]:
                new_time = time_so_far + travel_time

                if new_time < dist[next_node]:
                    # 더 빠른 길을 찾은 경우
                    dist[next_node] = new_time
                    ways[next_node] = ways[node]  # 지금까지 온 방법만큼 가능
                    heapq.heappush(heap, (new_time, next_node))
                elif new_time == dist[next_node]:
                    # 같은 최단 거리인 경우 → 경로 추가
                    ways[next_node] = (ways[next_node] + ways[node]) % MOD

        return ways[n - 1]  # 목적지까지 가는 모든 방법의 수