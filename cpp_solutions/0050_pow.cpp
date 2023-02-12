#include <iostream>

using namespace std;

double myPow(double x, int n) {
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return x;
    }
    if (n == INT32_MIN) {
        x = x * x;
        n = n / 2;
    }
    if (x == 1.) {
        return x;
    }
    double abs_x = x > 0? x: -x;
    double ans = abs_x;
    int abs_n = n > 0? n: -n;
    int n_ = 1;
    while (n_ <= abs_n / 2) {
        ans = ans * ans;
        n_ *= 2;
    }
    if (n_ < abs_n) {
        ans = ans * myPow(abs_x, abs_n - n_);
    }

    if (x < 0 && n % 2 == 1) {
        ans = -ans;
    }
    if (n < 0) {
        ans = 1 / ans;
    }

    return ans;
}

int main() {
    cout << myPow(-2, 3);
}