class TrieNode {
public:
    unordered_map<char, TrieNode*> trie;
    bool isEndOfWord;

    TrieNode() {
        isEndOfWord = false;
    }

    void insertWord(const string& word) {
        TrieNode* ptr = this;
        for (char c: word) {
            if (ptr->trie.find(c) == ptr->trie.end()) {
                ptr->trie[c] = new TrieNode();
            }
            ptr = ptr->trie[c];
        }

        ptr->isEndOfWord = true;
    }
};

class Solution {
public:
    vector<vector<int>> indexPairs(string text, vector<string>& words) {

        TrieNode* trie = new TrieNode();
        for (const string& word: words) {
            trie->insertWord(word);
        }
        vector<vector<int>> res;
        int n = text.length();
        for (int i = 0; i < n ; i++) {
            int temp = i;
            TrieNode* ptr = trie;
            while (temp < n && ptr->trie.find(text[temp]) != ptr->trie.end()) {
                ptr = ptr->trie[text[temp]];
                if (ptr->isEndOfWord) {
                    res.push_back({i, temp});
                }
                temp++;
            }
        }

        return res;



    }
};