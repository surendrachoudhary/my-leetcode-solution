class Solution:
    def shortestDistanceAfterQueries(self, n: int, q: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedSet
        p = SortedSet(range(n))
        ans = []

        for l,r in q:
            lb = p.bisect_left(l + 1)
            ub = p.bisect_left(r)

            del p[lb:ub]

            ans.append(len(p) - 1)

        return ans