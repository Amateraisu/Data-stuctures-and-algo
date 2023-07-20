class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        std::stack<int> stack;
        for (int a : asteroids) {
            if (a > 0) {
                stack.push(a);
            } else {
                while (!stack.empty() && stack.top() > 0 && std::abs(stack.top()) < std::abs(a)) {
                    stack.pop();
                }
                if (!stack.empty() && std::abs(a) == stack.top()) {
                    stack.pop();
                } else if (!stack.empty() && std::abs(a) < stack.top()) {
                    continue;
                } else {
                    stack.push(a);
                }
            }
        }
        std::vector<int> result(stack.size());
        for (int i = stack.size() - 1; i >= 0; --i) {
            result[i] = stack.top();
            stack.pop();
        }
        return result;
    }
};