#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* slow = head;
    ListNode* fast = head;
    ListNode* ans = slow;

    for (int i = 0; i < n; i++) {
        fast = fast->next;
    }

    if (!fast) {
        return head->next;
    }

    while (fast->next != nullptr) {
        fast = fast->next;
        slow = slow->next;
    }

    ListNode* nextnext = slow->next->next;
    slow->next = nextnext;

    return ans;
}

ListNode* create_list(vector<int>& nums) {
    ListNode* tail = new ListNode(0);
    ListNode* head = tail;
    for (auto el: nums) {
        tail->next = new ListNode(el);
        tail = tail->next;
    }
    return head->next;
}

void print_list(ListNode* list) {
    ListNode* ptr = list;
    while (ptr) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}

int main() {
    // vector<int> nums = {1, 2, 3, 4, 5};
    // int n = 2;

    // vector<int> nums = {1, 2, 3, 4, 5};
    // int n = 5;

    // vector<int> nums = {1, 2, 3, 4, 5};
    // int n = 1;

    // vector<int> nums = {1};
    // int n = 1;

    // vector<int> nums = {1, 2};
    // int n = 1;

    vector<int> nums = {1, 2};
    int n = 2;

    auto l = create_list(nums);
    auto l_ = removeNthFromEnd(l, n);
    print_list(l_);
}