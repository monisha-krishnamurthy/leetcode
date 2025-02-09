class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        psum_straight = [0]*len(nums)
        for i in range(1, len(nums)):
            psum_straight[i] = psum_straight[i-1] + nums[i-1]
        print(psum_straight)

        psum_reverse = [0]*len(nums)
        for j in range(len(nums)-2, -1, -1):
            psum_reverse[j] = psum_reverse[j+1] + nums[j+1]
        print(psum_reverse)
    
        for k in range(len(nums)):
            if psum_straight[k] == psum_reverse[k]:
                return k
        return -1


