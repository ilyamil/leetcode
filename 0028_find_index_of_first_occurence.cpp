#include <string>
#include <iostream>

using namespace std;

int strStr(string haystack, string needle) {
    int slow_ptr = 0;
    int N = haystack.length();
    int M = needle.length();
    while (slow_ptr < N - M + 1) {
        int fast_ptr = slow_ptr;
        bool flg = true;
        while (fast_ptr < N && (fast_ptr - slow_ptr < M)) {
            if (haystack[fast_ptr] != needle[fast_ptr - slow_ptr]) {
                flg = false;
                break;
            }
            fast_ptr++;
        }
        
        if (flg) {
            return slow_ptr;
        }
        slow_ptr++;
    }
    return -1;
}

int main() {
    string haystack = "sadbutsad";
    string needle = "g";
    cout << strStr(haystack, needle);
}