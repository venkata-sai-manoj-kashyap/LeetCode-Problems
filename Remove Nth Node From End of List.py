def removeNthFromEnd(head, n):
    count = 0
    ptr = head
    lis = []
    while ptr is not None:
        lis.append(ptr.val)
        ptr = ptr.next

    lis[-n] = None
    ptr = head
    if ptr.val != lis[0]:
        head = head.next
    while ptr is not None:
        if ptr.next is not None:
            print(1, lis[count + 1], ptr.next.val)
            if lis[count + 1] != ptr.next.val:
                if ptr.next.next is not None:
                    ptr.next.val = ptr.next.next.val
                    ptr.next.next = ptr.next.next.next
                    return head

                else:
                    ptr.next = None
                    return head
        count += 1
        ptr = ptr.next
    return head
