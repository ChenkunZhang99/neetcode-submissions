class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t) :
            return False
        freqs = {}
        freqt = {}
        for i in range (len(s)):
            freqs[s[i]] =  1 + freqs.get(s[i],0)
            freqt[t[i]] =  1 + freqt.get(t[i],0)
        return freqs == freqt