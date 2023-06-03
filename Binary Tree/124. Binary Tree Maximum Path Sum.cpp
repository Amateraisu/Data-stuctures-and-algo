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
    int res = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        // every node will return
        dfs(root);
        return res;
    }
    int dfs(TreeNode* root) {
        if (!root) return -2000;

        int left = dfs(root->left);
        int right = dfs(root->right);
        vector<int> comp = {res, root->val, left + root->val + right, root->val + left, root->val + right};
        vector<int> ret = {root->val, root->val + left, root->val + right};
        res = *max_element(comp.begin(), comp.end());

        return *max_element(ret.begin(), ret.end());
    }
};