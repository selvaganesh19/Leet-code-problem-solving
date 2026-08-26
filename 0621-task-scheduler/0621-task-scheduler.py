class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = defaultdict(int)

        for i in range(len(tasks)): m[tasks[i]]+=1
        count = m.values()
        maxc =  max(count)
        tied = sum(i==maxc for i in count)

        return max(len(tasks), (maxc-1)* (n+1)+ tied)