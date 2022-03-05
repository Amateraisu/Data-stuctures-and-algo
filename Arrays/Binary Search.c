
int search(int *nums, int numsSize, int target)
{
    int result = -1;

    int middle;
    int left = 0;
    int right = numsSize - 1;

    while (left <= right)
    {
        middle = (left + right) / 2;

        if (nums[middle] > target) // go to the left side;
        {
            right = middle - 1;
        }
        else if (nums[middle] < target) // go to the right side;
        {
            left = middle + 1;
        }
        else // found the element
        {

            result = middle;
            break;
        }
    }

    return result;
}