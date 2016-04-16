# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2=None):
    if l2 == None: l2 = []
    for i in l1:
        l2.append(i)
    return l2

def main():    
    list1 = ['cat', 'dog']
    nlist = append2list(list1)
    # nlist should be ['cat', 'dog']
    print(nlist)

    list2 = ['antelope']
    nlist = append2list(list2, ['lion'])
    # nlist should be ['lion', 'antelope']
    print(nlist)

    list3 = ['fox', 'chicken']
    nlist = append2list(list3)
    # nlist should be ['fox', 'chicken']
    print(nlist)

if __name__ == '__main__':
    main()
