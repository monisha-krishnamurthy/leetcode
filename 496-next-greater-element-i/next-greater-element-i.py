class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums2)
        mapping = defaultdict(lambda: -1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                res[stack[-1]] = nums2[i]
                mapping[nums2[stack[-1]]] = res[stack[-1]]
                stack.pop()
            stack.append(i)
        print(res)
        print(mapping)
        
        output = []
        for num in nums1:
            output.append(mapping[num])

        return output