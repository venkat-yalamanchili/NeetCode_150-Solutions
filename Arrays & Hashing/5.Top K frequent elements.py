from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        res = defaultdict(int)
        for num in nums:
            res[num] = 1 + res.get(num,0)
        sorted_items = sorted(res.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]