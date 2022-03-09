int numJewelsInStones(char * jewels, char * stones)
{
    int hashmap[129] = {0}; //number of ascii characters
    
    //indicate if its a jewel or not 
    
    
    char* ptr = jewels;
    int i = 0;
    int test = (int)jewels[0];
    
    //initiate the hashmap
    while(ptr[i] != '\0')
    {
        hashmap[(int)ptr[i]]=1;
        i++;
        
    }
    //jewel counter
    int total = 0;
    
    char* ptr2 = stones;
    int j = 0;
    
    while(ptr2[j] != '\0')
    {
        if (hashmap[(int)ptr2[j]] == 1)
        {
            total++;
        }
        
        
        j++;
    }
    return total;

}