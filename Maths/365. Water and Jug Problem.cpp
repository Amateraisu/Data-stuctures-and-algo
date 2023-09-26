class Solution {
public:
    int euclid (int a, int b) {
        if (b == 0) return a;

        return euclid(b, a % b);
    }
    bool canMeasureWater(int j1, int j2, int target) {
        if (j1 + j2 < target) return false;
        int t = euclid(j1, j2);
        if (target % t == 0) return true;

        return false;
    }
};
