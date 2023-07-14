/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    Node* cloneTree(Node* root) {

        return dfs(root);

    }

    Node* dfs(Node* node) {
        if (!node) return NULL;
        auto n = new Node(node->val);
        for (auto c :node->children) n->children.push_back(dfs(c));

        return n;
    }
};