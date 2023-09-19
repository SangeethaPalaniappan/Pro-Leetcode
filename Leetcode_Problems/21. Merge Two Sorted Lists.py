# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        Temp1 = list1
        Temp2 = list2
        
        if Temp1 == None:
            return Temp2
        elif Temp2 == None:
            return Temp1

        while Temp1 != None and Temp2 != None:
            if Temp1.val <= Temp2.val:
                head = self.Linkedlist(Temp1.val, head)
                Temp1 = Temp1.next
            elif Temp1.val > Temp2.val:
                head = self.Linkedlist(Temp2.val, head) 
                Temp2 = Temp2.next   
        if Temp1 == None:
           while Temp2 != None:
                head = self.Linkedlist(Temp2.val, head)
                Temp2 = Temp2.next
        elif Temp2 == None:
            while Temp1 != None:
                head = self.Linkedlist(Temp1.val, head)
                Temp1 = Temp1.next
        return head                




    def Linkedlist(self, val, head):
        tamp = head
        if head == None:
            head = ListNode(val)
            tamp = head
        else:
            while head.next != None:
                head = head.next
            head.next = ListNode(val)        
        return tamp


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''Temp1 = list1
        s1 = list1
        Temp2 = list2
        s2 = list2
        dup1 = Temp1
        dup2 = Temp2
        if Temp1 == None:
            return Temp2
        elif Temp2 == None:
            return Temp1
  
        while Temp1 != None and Temp2 != None:
            dup = Temp1
            Temp1 = Temp1.next
            if Temp1.val <= Temp2.val:
                s1 = recur(Temp1 , Temp2 , dup1)    
            elif Temp1.val > Temp2.val:
                s1 = recur(Temp2 , Temp1 , dup2) 

        return s1
def recur(Temp1 , Temp2 , dup):
    if Temp1 == None:
        dup.next = Temp2
    elif Temp1.val == Temp2.val :
        dup = Temp1 
        Temp1 = Temp1.next
        while Temp1 != None and Temp1.val == dup.val:
            dup = Temp1
            Temp1 = Temp1.next
        dup.next = Temp2
        
    elif Temp1.val >= Temp2.val:
        dup.next = Temp2   
    return recur(Temp1 , Temp2 , dup) '''