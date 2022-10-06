class Solution:
    def solve(self, s):
        # so just process all the digits first 
        res = []
        avail = []
        myMap = {}
        for char in s:
            if char.isnumeric():
                avail.append(int(char))
        avail.sort()
        greatest = avail[-1]
        smallest = avail[0]

        # do the ones 
        ones = int(s[-1])
        
        if ones < greatest:
            # find the next greatest element to replace 
            
            for num in avail:
                if num > ones:
                    
                    return s[0:4] + str(num)
        # append the smallest element and bring the carry over
        res.append(str(smallest))

        tenths = int(s[-2])
        # find the next greatest 
        
        for num in avail:
            if num > tenths:
                # check if valid 
                if num <= 5 :
                    return s[0:3] + str(num) + res[0]
 
        res = [str(smallest)] + res
        # else, caarry over to the main clock 
        # print(res)
        hourOnes = int(s[1])
        # find the next greatest 
        for num in avail:
            if num > hourOnes:
                if num <= 3 and int(s[0]) <= 2 or int(s[0]) != 2:
                    return s[0] + str(num) + ":" + "".join(res)


        res = [str(smallest)] + [":"] + res
        # print(res, "test 2")
        # now for hours 
        hour = int(s[0])
        for num in avail:
            if num > hour:
                if num <= 2:
                    return str(num) + "".join(res)
                break

        res = [str(smallest)] + res
                


        return "".join(res)