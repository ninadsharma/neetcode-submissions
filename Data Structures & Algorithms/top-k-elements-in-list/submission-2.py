class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqGraph = {x: nums.count(x) for x in nums}  
        #print(freqGraph)
        sortedGraph = dict(sorted(freqGraph.items(), key = lambda item: item[1], reverse = True))
        #print(sortedGraph)
        returnList = []
        for i in range(k):
            returnList.append(list(sortedGraph)[i])
        return returnList
