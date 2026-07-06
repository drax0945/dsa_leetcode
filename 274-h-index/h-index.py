class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        counts = [0]*(n+1)

        for i in citations:
            counts[min(i, n)] += 1

        h = n
        papers = counts[n]

        while papers<h:
            h -= 1
            papers += counts[h]
        return h