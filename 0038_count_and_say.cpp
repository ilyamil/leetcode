#include <iostream>
#include <string>

using namespace std;

string countAndSay(int n) {
    if (n == 1) {
        return "1";
    }

    string ans = "1";
    for (int i = 2; i <= n; i++) {
        int counter = 0;
        string ans_;
        for (int j = 0; j < ans.length(); j++) {
            if (j == 0) {
                counter++;
            }
            if ((j < ans.length() - 1 && ans[j] != ans[j + 1])
                || (j == ans.length() - 1)) {
                ans_ += to_string(counter) + ans[j];
                counter = 1;
            }
            else {
                counter++;
            }
        }
        ans = ans_;
    }
    return ans;
}

int main() {
    // 1, 11, 21, 1211, 111221

    cout << countAndSay(2) << '\n';
    cout << countAndSay(3) << '\n';
    cout << countAndSay(4) << '\n';
    cout << countAndSay(5) << '\n';
}