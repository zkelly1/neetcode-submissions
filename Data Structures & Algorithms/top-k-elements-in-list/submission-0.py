class Solution:
    import collections
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c: collections.Counter = collections.Counter(nums)

        return [ k for k, v in sorted(list(c.items()), key=lambda x: x[1], reverse=True)[:k]]

        