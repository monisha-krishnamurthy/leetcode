class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = list()
        # answer[0] = list(nums1.union(nums2))
        # answer.append(set())
        temp1 = set(nums1) - set(nums2)
        answer.append(list(temp1))
        temp2 = set(nums2) - set(nums1)
        answer.append(list(temp2))
        return answer

        # print(answer[0])