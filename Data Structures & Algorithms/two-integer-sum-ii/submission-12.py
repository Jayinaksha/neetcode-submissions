class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        stack = collections.deque()
        index = 0
        id = 0
        for i,num in enumerate(numbers):
            stack.append((i,num))
        i = 0
        while stack and i<len(numbers):
            if numbers[i] + stack[-1][1] > target:
                stack.pop()
            elif numbers[i] + stack[-1][1] < target:
                i += 1
            else:
                index, num = stack.pop()
                break
        if index < i:
            return [index+1, i+1]
        else:
            return [i+1, index+1]
