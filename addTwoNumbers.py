import time

class ListNode:
    def __inti__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(L1, L2):
    node = ListNode()
    res = node
    carry = 0
    endL1 = False
    endL2 = False
    while True:
        if not endL1:
            num1 = L1.val
            try:
                L1 = L1.next
            except AttributeError:
                endL1 = True
        else:
            num1 = None
        if not endL2:
            num2 = L2.val
            try:
                L2 = L2.next
            except AttributeError:
                endL2 = True
        else:
            num2 = None
        if num1 != None and num2 != None:
            total = num1 + num2 + carry
            if total > 9 and total != 10:
                carry = total%10
                total = abs(total - (10 * carry))
            elif total == 10:
                carry = 1
                total = 0
            res.next = ListNode()
            res.next.val = total
            res = res.next
        elif num1 != None and num2 == None:
            res.next = ListNode()
            res.next.val = num1
            res = res.next
        elif num1 == None and num2 != None:
            res.next = ListNode()
            res.next.val = num2
            res = res.next
        else:
            break
    res = node.next
    return res



def main():
    #tester 1
    dt1 = [2, 4, 3]
    dt2 = [5, 6, 4]
    node1 = ListNode()
    node2 = ListNode()
    L1 = node1
    L2 = node2
    for n in range(0, len(dt1)):
        L1.next = ListNode()
        L1.next.val = dt1[n]
        L1 = L1.next
        L2.next = ListNode()
        L2.next.val = dt2[n]
        L2 = L2.next
    
    L1 = node1.next
    L2 = node2.next
            

    out = addTwoNumbers(L1, L2)
    
    while out:
        print("{} => ".format(out.val), end="")
        try:
            out = out.next
        except:
            break



start =  time.time()
main()
print("{} seconds".format(time.time() - start))