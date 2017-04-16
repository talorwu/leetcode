"""
思路1：使用strs中元素的字典序作为key

思路2：
    collections.Counter creates a counter object. A counter object is like a specific kind of dictionary where it is build for counting (objects that hashes to same value)
    tuple(sorted(s)) is used here so that anagrams will be hashed to the same value. tuple is used because sorted returns a list which cannot be hashed but tuples can be hashed
    filter: selects some elements of the list based on given function (first argument - a lambda function is given here)
    lambda function defined here returns True if number of anagrams of that elements is greater than 1

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #strs.sort(key=lambda x: len(x))
        L = []
        for i in range(len(strs)):
            tmp = sorted(strs[i])
            tmp = "".join(tmp)
            L.append(tmp)
        #print L
        res = {}
        for i in range(len(L)):
            if L[i] not in res:
                res[L[i]] = [strs[i]]
            else:
                res[L[i]].append(strs[i])
            #print L[i],res[L[i]]
        return res.values()
        


def anagrams(self, strs):
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)
