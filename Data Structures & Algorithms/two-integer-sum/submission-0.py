class Solution:
    from collections import defaultdict 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = t     
        # b = t - a

        seen: dict[int, list[int]] = defaultdict(list)
        for idx, a in enumerate(nums):
            b: int = target - a

            if(b in seen):
                return sorted([idx, seen[b][0]])

            seen[a].append(idx)
            
            

