class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        final = []
        for word in words:
            if word == "":
                continue 
                
            final.append(word)
        print(final)
        return " ".join(reversed(final))