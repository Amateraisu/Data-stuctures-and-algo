class WordDictionary {
    struct TrieNode {
        unordered_map<char, TrieNode*> leaves;
        bool is_string = false;
    };
    TrieNode* root = nullptr;
public:
    WordDictionary() {
        root = new TrieNode();

    }

    void addWord(string word) {
        TrieNode* ptr = root;
        for (char& c: word) {
            if (ptr->leaves.count(c) == 0) {
                ptr->leaves[c] = new TrieNode();
            }
            ptr = ptr->leaves[c];
        }
        ptr->is_string = true;

    }
    bool doesExist(string& word, int index, TrieNode* ptr) {
        if (index == word.length()) {
            return ptr->is_string;
        }

        char cur = word[index];
        if (cur == '.') {
            // wild card
            for (auto it = ptr->leaves.begin(); it != ptr->leaves.end(); it++) {
                if (doesExist(word, index + 1, it->second)) return true;
            }

        } else {
            if (ptr->leaves.find(cur) != ptr->leaves.end()) {
                return doesExist(word, index + 1, ptr->leaves[cur]);

            }
        }
        return false;
    }

    bool search(string word) {
        return doesExist(word, 0, root);
    }
};