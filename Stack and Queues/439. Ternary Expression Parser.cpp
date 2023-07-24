class Solution {
public:
    string parseTernary(string expression) {

        int n = expression.length();
        int ptr = n - 1;
        string res = "";
        stack<char>operators, operands;

        while (ptr >= 0) {
            char current = expression[ptr];
            if (current == '?') {
                char first = operands.top();
                operands.pop();
                char second = operands.top();
                operands.pop();
                if (expression[ptr - 1] != 'F') {
                    operands.push(first);
                } else {
                    operands.push(second);
                }
                ptr -= 2;

            } else if (current == ':') {
                operators.push(current);
                ptr--;

            } else {
                operands.push(current);
                ptr--;
            }

        }
        res += operands.top();
        return res;



    }
};