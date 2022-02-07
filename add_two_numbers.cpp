#include <iostream>
#include <vector>


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int sum = l1->val + l2->val;
    int resid = sum / 10;
    ListNode* tail = new ListNode(sum % 10);
    ListNode* head = new ListNode(-1, tail);
    l1 = l1->next;
    l2 = l2->next;
    while (l1 != nullptr || l2 != nullptr) {
        sum = resid;
        if (l1 != nullptr) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != nullptr) {
            sum += l2->val;
            l2 = l2->next;
        }
        resid = sum / 10;
        ListNode* tail_segment = new ListNode(sum % 10);
        tail->next = tail_segment;
        tail = tail->next;
    }
    if (resid > 0) {
        tail->next = new ListNode(resid);
        tail = tail->next;
    }
    return head->next;
}


ListNode* create_list(const std::vector<int>& elements) {
    ListNode* tail = new ListNode(elements[0]);
    ListNode* head = new ListNode(-1, tail);
    if (elements.size() > 1) {
        for (int i = 1; i < elements.size(); i++) {
            tail->next = new ListNode(elements[i]);
            tail = tail->next; 
        }
    }
    return head->next;
}


void print_list(ListNode* l) {
    while (l != nullptr) {
        if (l->next == nullptr) {
            std::cout << l->val;
        }
        else {
            std::cout << l->val << " -> ";
        }
        l = l->next;
    }
    std::cout << std::endl;
}


int main() {
    ListNode* l1 = create_list({9,9,9,9,9,9,9});
    ListNode* l2 = create_list({9,9,9,9});
    auto sum = addTwoNumbers(l1, l2);
    print_list(sum);
}