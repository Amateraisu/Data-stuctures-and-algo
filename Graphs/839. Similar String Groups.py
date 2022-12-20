class Solution:
    def numSimilarGroups(self, strings: List[str]) -> int:
        # for every node, connect another node such that 
        # t a r s  
        # r a t s 
        # a r t s 

        # ==== 1 group ====== 
        # s t a r 
        # 300 x 300 = 9 x 10 * 4 
        # 9 x 10**4 x 300 = 12 * 10**6 = 1.2 * 10**7
        # so for every string, try to connect a string to a group. 
        # so how do I see if there is a group? 
        if len(strings) == 1:
            return 1
        parents = [i for i in range(len(strings))]
        rank = [1 for i in range(len(strings))]
        res = len(strings)
        n = len(strings)
        def find(index):
            # here we find the parent of the currentString 
            current = index 
            while current != parents[current]:
                current = parents[current]
            return current

        def union(par1, par2):
            p1, p2 = find(par1), find(par2)
            if p1 == p2:
                return 0 
            
            # join the 2 strings here 
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                rank[p2] = rank[p1]
                parents[p2] = parents[p1]
            else:
                rank[p2] += rank[p1]
                rank[p1] = rank[p2]
                parents[p1] = parents[p2]

            return -1         




        for i in range(n):
            for j in range(i + 1, n):
                string1 = strings[i]
                string2 = strings[j]

                if parents[i] == parents[j] :
                    continue
                    
                elif group(string1, string2):
                    res += union(i, j)

        return res
        
def group(string1, string2):
    diff = 0 
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff += 1   
    return diff == 2 or diff == 0 