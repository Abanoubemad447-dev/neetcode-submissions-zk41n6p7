
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =Counter(nums)
        res=[]
        Topk=count.most_common(k)
        for num,freq in Topk:
            res.append(num)
        return res    
        

