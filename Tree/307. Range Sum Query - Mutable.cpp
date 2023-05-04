


class NumArray {
  int n;
  vector<int> tree;
  public:
    void buildTree(vector<int>& nums) {
      for (int i = 0; i < nums.size(); i++) {
        tree[n + i] = nums[i];
      }

      for (int i = n - 1; i >= 0; i--) {
        tree[i] = tree[2 * i] + tree[2 * i + 1];
      }
      // done building already
    }

    int query(int left, int right) {
      int res = 0;
      left += n;
      right += n;
      while (left <= right) {
        if (left % 2 == 1) {
          res += tree[left];
          left++;
        }
        if (right % 2 == 0) {
          res += tree[right];
          right--;
        }

        left/=2;
        right /=2;
      }
      return res;

    }





    NumArray(vector<int>& nums) {
      n = nums.size();
      tree.resize(2 * n, 0);
      buildTree(nums);

    }

    void update(int index, int val) {

      index += n;
      int left = index;
      int right = index;
      tree[index] = val;
      while (index > 0) {
        left = right = index;
        if (index % 2 == 0) {
          right++;
        } else {
          left--;
        }
        tree[index/2] = tree[left] + tree[right];
        index /= 2;


      }
      return;
    }

    int sumRange(int left, int right) {
      return query(left, right);


    }
};