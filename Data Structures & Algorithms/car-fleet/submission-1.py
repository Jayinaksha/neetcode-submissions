class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0.0] * len(position)
        car = sorted(zip(position,speed), reverse=True)
        pos = [pos for pos, spd in car]
        spd = [spd for pos, spd in car]
        for i in range(len(position)):
            time[i] = (target - pos[i])/ spd[i]
        stack = collections.deque()
        for t in time:
            if stack and t > stack[-1]:
                stack.append(t)
            if not stack:
                stack.append(t)
        return len(stack)