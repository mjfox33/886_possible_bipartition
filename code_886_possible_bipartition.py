from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        if n == 1 or not dislikes:
            return True

        worker = {i:set() for i in range(1,n+1)}
        for p1, p2 in dislikes:
            worker[p1].add(p2)
            worker[p2].add(p1)
        
        color1 = set()
        color2 = set()

        skipped = deque()
        for i in range(1,n+1):
            if not color1 and not color2:
                color1.add(i)

            bad = set()
            good = set()
            if i in color1:
                bad = color1
                good = color2
            elif i in color2:
                good = color1
                bad = color2

            if bad:
                for p2 in worker[i]:
                    if p2 in bad:
                        return False
                    good.add(p2)
            else:
                c1_bad = any(p2 in color1 for p2 in worker[i])
                c2_bad = any(p2 in color2 for p2 in worker[i])
                if c1_bad and c2_bad:
                    return False
                if c1_bad:
                    color2.add(i)
                elif c2_bad:
                    color1.add(i)
                else:
                    skipped.append(i)
        while skipped:
            i = skipped.popleft()
            c1_bad = any(p2 in color1 for p2 in worker[i])
            c2_bad = any(p2 in color2 for p2 in worker[i])
            if c1_bad and c2_bad:
                return False
            if c1_bad:
                color2.add(i)
            else:
                color1.add(i)
                
        return True