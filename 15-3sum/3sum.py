class Solution:
    # BRUTE FORCE SOLUTION
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1

        res = []
        for i in range(len(nums)):
            count_dict[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, len(nums)):
                count_dict[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                search = -(nums[i] + nums[j]) 
                if count_dict[search] > 0:
                    res.append([nums[i], nums[j], search])

            for j in range(i + 1, len(nums)):
                count_dict[nums[j]] += 1
        return res

# TIME-COMPLEXITY: O(n^3)
# SPACE-COMPLEXITY: O(n) 



