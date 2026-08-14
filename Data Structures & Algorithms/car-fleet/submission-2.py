class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        max_time = 0
        car = sorted(zip(position,speed), reverse=True)
        for pos, spd in car:
            time = (target - pos)/ spd
            if time > max_time:
                fleet += 1
                max_time = time 
        return fleet