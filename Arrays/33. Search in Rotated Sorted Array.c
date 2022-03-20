// we can first do a normal binary search to find the smallest number

// Then we just do a binary search from there on
int search(int *nums, int numsSize, int target)
{
    int left = 0, right = numsSize - 1;

    while (left < right)
    {
        int middle = left + (right - left) / 2;

        if (nums[right] > nums[middle])
        {
            // this is normal, search the left side
            right = middle;
        }
        else
        {
            left = middle + 1;
        }
    }

    int start = left;

    left = 0;

    right = numsSize - 1;

    if (target >= nums[start] && target <= nums[right])
    {
        left = start;
    }
    else
    {
        right = start;
    }

    while (left <= right)
    {
        int middle = left + (right - left) / 2;

        if (nums[middle] == target)
        {
            return middle;
        }
        else if (target < nums[middle])
        {

            right = middle - 1;
        }
        else
        {

            left = middle + 1;
        }
    }

    return -1;
}