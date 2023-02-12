#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Time complexity: O(n^2)
// void decode(string s, int i, int& cnt) {
//     if (i >= s.length()) {
//         cnt++;
//         return;
//     }

//     if (s[i] != '0') {
//         decode(s, i + 1, cnt);
//         if (i < s.length() - 1 && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) {
//             decode(s, i + 2, cnt);
//         }
//     }
// }

// int numDecodings(string s) {
//     if (s[0] == '0') {
//         return 0;
//     }

//     int cnt = 0;
//     decode(s, 0, cnt);
//     return cnt;
// }


int numDecodings(string s) {
    int N = s.length();
    vector<int> dp(N + 1);
    dp[N] = 1;
    int cnt = 0;
    for (int i = N - 1; i >= 0; i--) {
        if (s[i] == '0') {
            dp[i] = 0;
        }
        else {
            dp[i] = dp[i + 1];
            if (i < s.length() - 1 && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) {
                dp[i] += dp[i + 2];
            }        
        }
    }
    return dp[0];
}


int main() {
    // string s = "226";
    // string s = "11106";
    // string s = "12";
    string s = "27";
    cout << numDecodings(s);
}