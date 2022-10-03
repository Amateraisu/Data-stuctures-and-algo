class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        # for every num, dump the bits into pockets 
        
        bins = [0] * 32 
        for num in nums:
            for i in range(0, 32):
                if num & 1 << i != 0:
                    bins[i] += 1 

        res = 0       
        # for the bins with odd number, try to change it to an even number 
        for index, bucket in enumerate(bins):
            if bucket == 0:
                continue 
            else:
                res |= 1 << index
                
        return res