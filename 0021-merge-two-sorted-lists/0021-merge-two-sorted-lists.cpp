/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* res=new  ListNode(-1);
         ListNode* temp=res;
          ListNode* left=list1;
         ListNode* right=list2;  
         while(left!=NULL&&right!=NULL){
             if(left->val<right->val){
                 res->next=left;
                 res=res->next;
                 left=left->next;
                 }
                else{
                 res->next=right;
                 res=res->next;
                 right=right->next;
                 }
         }
          while(left!=NULL){
             
                 res->next=left;
                 res=res->next;
                 left=left->next;
                 
         }
          while(right!=NULL){
             
                 res->next=right;
                 res=res->next;
                 right=right->next;
                 
         }

     return temp->next;
    }
};