class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {} 
        for word in strs :
            new_word = "".join(sorted(word))
            if new_word not in freqs:
                freqs[new_word] = []
            freqs[new_word].append(word)

        return list(freqs.values())