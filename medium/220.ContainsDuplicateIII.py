
"""
http://www.tuicool.com/articles/iE3imiQ
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1,t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return False

            



public class Solution {
	public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
		if(k < 1 || t < 0)
			return false;
		TreeSet<Integer> set = new TreeSet<>();
		for(int i = 0; i < nums.length; i++){
			int n = nums[i];
			if(set.floor(n) != null && n <= t + set.floor(n) || 
					set.ceiling(n) != null && set.ceiling(n) <= t + n)
				return true;
			set.add(n);
			if (i >= k)
				set.remove(nums[i - k]);
		}
		return false;
	}
}
