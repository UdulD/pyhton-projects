def TOH(n,source,to,helper):
    if n==1:
        print('move disk 1 from',source,'to',to)
        return
    TOH(n-1,source,helper,to)
    print('move disk',n,'from',source,'to',to)
    TOH(n-1,helper,to,source)

TOH(3,'A','C','B')