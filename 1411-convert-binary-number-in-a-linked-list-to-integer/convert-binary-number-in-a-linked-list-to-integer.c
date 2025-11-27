/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
int tot=0;
    while(head!=NULL){
  
    tot = tot*2+head->val;
    head= head->next;

    }
    return tot;
    
}