#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<int> inorder(TreeNode* root) {
    stack<TreeNode*> st;
    vector<int> ordered_nums;
    TreeNode* cur = root;
    while (!st.empty() || cur != NULL) {
        while (cur) {
            st.push(cur);
            cur = cur->left;
        }
        cur = st.top();
        st.pop();
        ordered_nums.push_back(cur->val);
        cur = cur->right;
    }

    return ordered_nums;
}

bool isValidBST(TreeNode* root) {
    if (!root) {
        return true;
    }
    vector<int> nums = inorder(root);
    for (int i = 0; i < nums.size(); i++) {
        if (i > 0 && nums[i] <= nums[i - 1]) {
            return false;
        }
    }
    return true;
}


int main() {
    TreeNode* A = new TreeNode(8);
    A->left = new TreeNode(3);
    A->right = new TreeNode(10);
    A->left->left = new TreeNode(1);
    A->left->right = new TreeNode(6);
    A->left->right->left = new TreeNode(4);
    A->left->right->right = new TreeNode(7);
    A->right->right = new TreeNode(11);
    A->right->right->right = new TreeNode(15);

    auto nums = inorder(A);
    for (auto num: nums) {
        cout << num << ' ';
    }
}