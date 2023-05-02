class Solution {
public:
    double average(vector<int>& salary) {
        int maxi = *max_element(salary.begin(), salary.end());

        int mini = *min_element(salary.begin(), salary.end());
        int res = 0;
        int c = 0;
        int n = salary.size();
        for (int i = 0; i < n ;i++) {
            if (salary[i] != maxi && salary[i] != mini) {
                res += salary[i];
                c++;
            }
        }

        return (long double)res /c ;
    }
};