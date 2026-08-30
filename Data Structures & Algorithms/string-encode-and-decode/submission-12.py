class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted = ""
        for word in strs:
            encrypted += str(len(word)) + "#" + word
        return encrypted
    def decode(self, s: str) -> List[str]:
        decrypted_list = []
        curr = 0

        while curr < len(s):
            index = s.index("#",curr)
            length = int(s[curr:index])
            decrypted_list.append(s[index+1: index+1+length])
            curr = index + length+1 

        return decrypted_list

                

            