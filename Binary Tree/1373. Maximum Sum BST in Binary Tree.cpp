/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int res;
public:
    int maxSumBST(TreeNode* root) {
        res = 0;

        dfs(root);

        return res;
    }

    vector<int> dfs(TreeNode* node) {
        if (!node) {
            return {INT_MAX, 0, INT_MIN};

        }

        vector<int> l = dfs(node->left);
        vector<int> r = dfs(node->right);
        if (node-> val < r[0] && node->val > l[2]) {
            res = max(res, node->val + r[1] + l[1]);

            return {min({node->val, l[0], r[0]}),node->val + r[1] + l[1], max({r[2], node->val, l[2]})};
        }

        return {INT_MIN, 0, INT_MAX};




    }
};