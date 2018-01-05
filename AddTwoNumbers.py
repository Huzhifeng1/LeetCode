import math
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        listnum1 = []
        listnum2 = []
        while l1 != None:
            listnum1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            listnum2.append(l2.val)
            l2 = l2.next
        num1 = long(0)
        num2 = long(0)
        po = long(1)

        for i in range(len(listnum1)):
            temp1 = long(listnum1[i])
            temp2 = po
            num1 = num1 + temp1 * temp2
            po = str(po) + '0'
            po = long(po)
        po = long(1)

        for i in range(len(listnum2)):
            temp1 = long(listnum2[i])
            temp2 = po
            num2 = num2 + temp1 * temp2
            po = str(po) + '0'
            po = long(po)

        num = num1+num2
        str1 = str(num)
        result = []
        for i in str1:
            result.append(int(i))
        result = list(reversed(result))
        return result




