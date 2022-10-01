#include <iostream>
#include <vector>

using namespace std;

int maxArea(vector<int>& height) {
    int max_area = 0;
    int area = 0;
    int left = 0;
    int right = height.size() - 1;
    while (left != right) {
        if (height[left] > height[right]) {
            area = (right - left) * height[right];
            right--;
        }
        else {
            area = (right - left) * height[left];
            left++;
        }
        max_area = max(max_area, area);
    }

    return max_area;
}

int main() {
    vector<int> A = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << maxArea(A);
}