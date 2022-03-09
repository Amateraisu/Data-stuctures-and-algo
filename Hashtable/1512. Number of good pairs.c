int numIdenticalPairs(int* nums, int numsSize)
{
    int i, total = 0;
    
    int hashmap[101] = {0};
    
    for (int i = 0; i<numsSize; i++)
    {
        hashmap[nums[i]]++;
        if (hashmap[nums[i]] >1 )
        {
            total+= hashmap[nums[i]]-1;
            
        }
        
        
    }
    
    return total;
    

}