from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        queue1 = deque()
        queue2 = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                queue1.append(i)
            elif senate[i] == "D":
                queue2.append(i)

        while(queue1 and queue2):
            for i in range(len(senate)):
                if queue1[0] == i:
                    queue1.popleft()
                    queue2.popleft()
                    queue1.append(i)
                elif queue2[0] == i:
                    queue2.popleft()
                    queue1.popleft()
                    queue2.append(i)
                if not queue1 or not queue2:
                    break

        if not queue1:
            return "Dire"
        elif not queue2:
            return "Radiant"
