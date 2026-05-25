class Solution:
    def groupAnagrams(strs):
        ans = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        return list(ans.values())