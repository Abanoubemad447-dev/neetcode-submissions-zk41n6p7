class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      counted_nums=Counter(nums)
      result=[]
      return[num for num, _ in counted_nums.most_common(k)]