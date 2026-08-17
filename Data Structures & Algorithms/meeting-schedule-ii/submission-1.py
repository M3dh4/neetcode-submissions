"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s=sorted([i.start for i in intervals])
        e=sorted([i.end for i in intervals])
        res,count=0,0
        st,ed=0,0
        while st<len(intervals):
            if s[st]<e[ed]:
                st+=1
                count+=1
            else:
                ed+=1
                count-=1
            res=max(res,count)
        return res