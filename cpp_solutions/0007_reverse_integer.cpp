#include <iostream>

using namespace std;

int reverse(int x) {
    if (x == INT32_MIN) {
        return 0;
    }

    bool positive = x >= 0? 1: 0;
    x = abs(x);

    int reversed_x = 0;
    while (x > 0) {
        if (reversed_x > INT32_MAX / 10) {
            return 0;
        }
        reversed_x = reversed_x * 10 + x % 10;
        x /= 10;
    }

    return positive? reversed_x: -reversed_x;
}

int main() {
    int A = INT32_MAX;
    std::cout << reverse(A);
}