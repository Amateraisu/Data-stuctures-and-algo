


//1. merge sort nlogn 
//2. in the sorted array, u check for duplicates. O(n)  nlogn


void merge(int* num, int left , int middle, int right)
{
    int leftnum = middle - left+1;
    int rightnum = right- middle;
    
    int leftarr[leftnum];
    int rightarr[rightnum];
    
    int i =0;
    int j = 0 ;
    int k = left;
    
    for (int i = 0 ; i<leftnum; i++)
    {
        leftarr[i] = num[left+i];
        
    }
    for (int j = 0 ; j<rightnum; j++)
    {
        rightarr[j] = num[middle+1+j];
        
    }
    
    i = j = 0;
    
    while (i<leftnum && j <rightnum)
    {
        if (leftarr[i]<=rightarr[j])
        {
            num[k]=leftarr[i];
            k++;
            i++;
        }
        else 
        {
            num[k]=rightarr[j];
            j++;
            k++;
        }
    }
    
    while (i<leftnum)
    {
        num[k] = leftarr[i];
        k++;
        i++;
        
    }
    while (j<rightnum)
    {
        num[k] = rightarr[j];
        k++;
        j++;
        
    }
    
}


void mergesort(int* arr, int left, int right)
{
    if (left < right)
    {
        int middle = (left+right)/2;
        mergesort(arr, left, middle);
        mergesort(arr,middle+1, right);
        merge(arr, left, middle,right);
    }
}



bool containsDuplicate(int* nums, int numsSize)
{
    mergesort(nums,0, numsSize -1);
    int counter = 0;
    int i = 0;
    int j = 1;
    
    while (i<numsSize-1)
    {
        if (nums[j]==nums[i])
        {
            counter++;
            return true;
        }
        j++;
        i++;
    }
    
    return false;
    
    

}