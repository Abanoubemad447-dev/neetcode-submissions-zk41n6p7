class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # The 'if' statement is now perfectly aligned under 'diff'
            if diff in map:
                return [map[diff], i]
                
            map[n] = i