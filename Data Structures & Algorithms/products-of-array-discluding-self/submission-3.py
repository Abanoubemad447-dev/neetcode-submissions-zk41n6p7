class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        # Sweep 1: Multiply everything to the LEFT of the index
        left_prod = 1
        for i in range(n):
            res[i] = left_prod
            left_prod *= nums[i]

        # Sweep 2: Multiply everything to the RIGHT of the index
        right_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]

        return res