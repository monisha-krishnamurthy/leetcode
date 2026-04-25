class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = defaultdict(int)
        output = [0]*len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack[-1]] = num
                stack.pop() 
            stack.append(num)

        for i,num in enumerate(nums1):
            if num in mapping:
                output[i] = mapping[num]
            else:
                output[i] = -1
        return output