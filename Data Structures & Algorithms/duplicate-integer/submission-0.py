class Solution:
    import collections 
    def hasDuplicate(self, nums: List[int]) -> bool:
        c: collections.Counter = collections.Counter(nums)

        return any(v > 1 for k, v in c.items())