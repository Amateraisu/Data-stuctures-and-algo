

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
    // first copy nums1 into another temp array;

    if (m != 0) // if first array has elements
    {
        int temp[m];
        int k = 0;
        int i = 0;
        int j = 0;

        while (i < m)
        {

            temp[i] = nums1[i];
            i++;
        }

        i = 0;

        while (i < m && j < n)
        {
            if (temp[i] <= nums2[j])
            {
                nums1[k] = temp[i];
                i++;
            }
            else
            {
                nums1[k] = nums2[j];
                j++;
            }

            k++;
        }
        while (i < m)
        {
            nums1[k] = temp[i];
            i++;
            k++;
        }
        while (j < n)
        {
            nums1[k] = nums2[j];
            j++;
            k++;
        }
    }
    else // copy all num2 arrays into num1
    {
        int i = 0;
        while (i < n)
        {
            nums1[i] = nums2[i];
            i++;
        }
    }
}