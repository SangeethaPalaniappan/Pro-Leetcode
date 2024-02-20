# 1791. Find Center of Star Graph

class Solution:
    def findCenter(self, edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:            
            return edges[0][1]