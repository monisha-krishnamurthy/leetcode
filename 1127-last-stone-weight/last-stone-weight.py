class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n > 1:
            curr = stones.pop() - stones.pop()
            n -= 2

            if curr > 0:
                l, r = 0, n
                while l < r:
                    mid = (l + r) // 2
                    if curr > stones[mid]:
                        l = mid + 1
                    else:
                        r = mid
                pos = l
                n += 1
                stones.append(0)
                for i in range(n-1, pos-1, -1):
                    stones[i] = stones[i -1]
                stones[pos] = curr
        return stones[0] if stones else 0
