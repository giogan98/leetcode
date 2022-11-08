'''
You are given an array of integers stones where stones[i] is the weight of the
ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two
stones and smash them together. Suppose the heaviest two stones have weights x
and y with x <= y. The result of this smash is:

    - If x == y, both stones are destroyed, and
    - If x != y, the stone of weight x is destroyed, and the stone of weight y 
      has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left,
return 0.
'''

from typing import List

# Method1, not very efficient as we sort the list if the numbers arent the same
class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort(reverse=True)
        
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
                stones.sort(reverse=True)
        
        if len(stones) == 0:
            return 0
        return stones[0]

# Method2, insert the stone in the correct place instead of sorting the list
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def insertIntoList(lst: List[int], num: int) -> List:
            first, middle, last = 0, 0, len(lst)
            print("Before: ", lst)
            while first < last:
                middle = (first + last) // 2
                if lst[middle] < num:
                    last = middle
                else:
                    first = middle + 1
            lst.insert(first, num)
            print("After: ", lst)
            return lst            

        stones.sort(reverse=True)
        
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                num = stones.pop(0) - stones.pop(0)
                stones = insertIntoList(stones, num)
        
        if len(stones) == 0:
            return 0
        return stones[0]

def main():
    solution = Solution2()

    stones1 = [2,7,4,1,8,1]
    stones2 = [1]
    stones3 = [3, 7, 8]

    print(solution.lastStoneWeight(stones1))
    print(solution.lastStoneWeight(stones2))
    print(solution.lastStoneWeight(stones3))

if __name__ == '__main__':
    main()