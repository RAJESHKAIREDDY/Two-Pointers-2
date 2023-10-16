#Time Complexity: O(N)
#Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=1
        count=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                count +=1
            else:
                count=1
            if count<=2:
                nums[slow]=nums[i]
                slow +=1
        return slow
        