class Solution {
public:
    string predictPartyVictory(string senate) {
        int net = 0;
        vector<char> stack(senate.begin(), senate.end());


        while (true) {
            vector<char> new_stack;
            bool should = false;
            for (char s: stack) {
                if (s == 'D') {
                    net++;
                    if (net > 0) {
                        new_stack.push_back(s);
                    } else {
                        should = true;
                    }
                } else {
                    net--;
                    if (net < 0) {
                        new_stack.push_back(s);
                    } else {
                        should = true;
                    }
                }
            }

            stack = new_stack;
            if (!should) {
                break;
            }

        }

        if (net > 0) return "Dire";

        return "Radiant";

    }
};