class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1

        return count