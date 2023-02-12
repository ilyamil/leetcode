#include <iostream>
#include <map>
#include <string>

using namespace std;


int myAtoi(string s) {
    map<char, int> digits = {
        {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3},
        {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7},
        {'8', 8}, {'9', 9}
    };

    bool positive = true;
    bool significant = false;

    int i = 0;
    // skip whitespaces
    while (s[i] == ' ') {
        i++;
    }

    // if not plus or minus sign return 0
    if (digits.find(s[i]) == digits.end() && s[i] != '-' && s[i] != '+') {
        return 0;
    }

    // check a sign
    if (s[i] == '+') {
        if (i != s.length() - 1 && digits.count(s[i + 1]) == 0) {
            return 0;
        }
        i++;
    }
    if (s[i] == '-') {
        positive = false;
        if (i != s.length() - 1 && digits.count(s[i + 1]) == 0) {
            return 0;
        }
        i++;
    }

    int my_integer = 0;
    while (i != s.length() && digits.count(s[i]) == 1) {
        if (positive) {
            if ((my_integer > INT32_MAX / 10)
                || (my_integer == INT32_MAX / 10 && digits[s[i]] > 7)) {
                return INT32_MAX;
            }
        }
        if (!positive) {
            if ((my_integer > INT32_MAX / 10)
                || (my_integer == INT32_MAX / 10 && digits[s[i]] >= 8)) {
                return INT32_MIN;
            }
        }
        my_integer = my_integer * 10 + digits[s[i]];
        i++;
    }

    return positive? my_integer: -my_integer;
}

int main() {
    // string A = "-2147483647";
    // string A = "-2147483648";
    // string A = "9999999999999";
    string A = "-2147483648";
    int B = atoi(A.c_str());
    cout << B << " " << myAtoi(A);
}