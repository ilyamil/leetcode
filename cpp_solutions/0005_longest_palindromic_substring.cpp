#include <iostream>

using namespace std;

string longestPalindrome(string s) {
    if (s.length() == 0) {
        return s;
    }

    int len = 0;
    int L = 0;
    int R = 0;

    for (int i = 0; i < s.length(); i++) {
        // even case
        int l = i;
        int r = i + 1;
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            if (r - l + 1 > len) {
                len = r - l + 1;
                L = l;
                R = r;
            }
            l--;
            r++;
        }
        // odd case
        int lo = i;
        int ro = i;
        while (lo >= 0 && ro < s.length() && s[lo] == s[ro]) {
            if (ro - lo + 1 > len) {
                len = ro - lo + 1;
                L = lo;
                R = ro;
            }
            lo--;
            ro++;
        }
    }

    return s.substr(L, len);
}

int main() {
    // string A = "abad";
    // std::cout << longestPalindrome(A);

    // string A = "ababa";
    // std::cout << longestPalindrome(A);

    // string A = "abc";
    // std::cout << longestPalindrome(A);
    
    string A = "abcaa";
    std::cout << longestPalindrome(A);
}