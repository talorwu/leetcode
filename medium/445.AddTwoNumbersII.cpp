/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        l1 = reverse(l1);
        l2 = reverse(l2);
        ListNode *head,*ans;
        *head = *ans = new ListNode(-1);
        int carry = 0;
        while(l1 || l2 || carry){
            int tmp = carry;
            if(l1){tmp+=l1->val;l1 = l1->next;}
            if(l2){tmp+=l2->val;l2 = l2->next;}
            carry = tmp /10;
            tmp %= 10;
            ListNode *a = new ListNode(tmp);
            ans->next = a;
            ans = a;
        }
        ans = reverse(head->next);
        return ans;
    }
    
    ListNode * reverse(ListNode *l){
        ListNode * pre = NULL,*cur = l;
        while(cur){
            ListNode * tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
};
