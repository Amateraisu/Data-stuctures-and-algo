class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashOfAnagrams = {}
        for index,string in enumerate(strs):
            key = tuple(sorted(string))
            if key not in hashOfAnagrams:
                hashOfAnagrams[key] = [index]
            else:
                hashOfAnagrams[key].append(index)
                
        res = [[strs[index] for index in hashOfAnagrams[key]] for key in hashOfAnagrams]
        return res