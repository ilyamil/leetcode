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

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* tail = new ListNode(0);
    ListNode* head = tail;


    int rem = 0;
    int s = 0;
    while (l1 || l2) {
        s = rem;
        if (l1) {
            s += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            s += l2->val;
            l2 = l2->next;
        }
        if (s > 9) {
            rem = 1;
            s -= 10;
        }
        else {
            rem = 0;
        }
        tail->next = new ListNode(s);
        tail = tail->next;
    }

    if (rem) {
        tail->next = new ListNode(rem);
        tail = tail->next;
    }
    return head->next;
}

ListNode* construct_linked_list(const vector<int> &nums) {
    ListNode* tail = new ListNode();
    ListNode* head = tail;

    for (const int el: nums) {
        tail->next = new ListNode(el);
        tail = tail->next;
    }
    return head->next;
}

int main() {
    // ListNode* A = new ListNode(2);
    // A->next = new ListNode(4);
    // A->next->next = new ListNode(3);

    // ListNode* B = new ListNode(5);
    // B->next = new ListNode(6);
    // B->next->next = new ListNode(4);

    // auto ans = addTwoNumbers(A, B);
    // while (ans) {
    //     std::cout << ans->val << ' ';
    //     ans = ans->next;
    // }

    // ListNode* A = new ListNode(0);
    // ListNode* B = new ListNode(0);

    // auto ans = addTwoNumbers(A, B);
    // while (ans) {
    //     std::cout << ans->val << ' ';
    //     ans = ans->next;
    // }

    ListNode* A = construct_linked_list({9,9,9,9,9,9,9});
    ListNode* B = construct_linked_list({9,9,9,9});

    auto ans = addTwoNumbers(A, B);
    while (ans) {
        std::cout << ans->val << ' ';
        ans = ans->next;
    }

// l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]
}