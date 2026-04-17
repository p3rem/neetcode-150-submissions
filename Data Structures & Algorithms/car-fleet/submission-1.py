class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevtime = (target - pair[0][0])/ pair[0][1]
        for i in range(1,len(pair)):
            curcar = pair[i]
            curtime = (target - curcar[0])/curcar[1]
            if curtime > prevtime:
                fleets += 1
                prevtime = curtime 
        return fleets 