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

public:
    double res = 0;
    double maximumAverageSubtree(TreeNode* root) {

        dfs(root);
        return res;
    }

    pair<double, double> dfs(TreeNode* n) {
        if (!n) return {0, 0};
        pair<double, double> l = dfs(n->left);
        pair<double, double> r = dfs(n->right);
        res = max(res, (l.first + r.first + n->val)/(l.second + r.second + 1));
        return {l.first + r.first + n->val, l.second + r.second + 1};
    }
};