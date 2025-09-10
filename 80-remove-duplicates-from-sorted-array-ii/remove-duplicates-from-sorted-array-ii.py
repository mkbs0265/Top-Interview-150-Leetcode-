class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return 2
        l=2
        for i in range(2,n):
            if nums[i]!=nums[l-2]:
                nums[l]=nums[i]
                l+=1
        return l