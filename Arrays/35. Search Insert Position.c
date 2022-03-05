// binary search

int searchInsert(int *nums, int numsSize, int target)
{
    int left = 0;
    int right = numsSize - 1;
    while (left <= right)
    {
        int middle = (left + right) / 2;

        if (nums[middle] > target) // move to the left
        {
            right = middle - 1;
            if (right < left)
            {
                return left;
            }
        }
        else if (nums[middle] < target) // move to the right
        {
            left = middle + 1;
            if (left > right)
            {
                return left;
            }
        }
        else if (nums[middle] == target) // target found
        {
            return middle;
        }
    }; // breaking out of the while loop means i didnt find it

    return 0;
}
