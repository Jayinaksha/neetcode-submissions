class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        array = [0] * len(temperatures)
        stack = collections.deque()
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                array[prev] = i - prev
            stack.append(i)
        return array