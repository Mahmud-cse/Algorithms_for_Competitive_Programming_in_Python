"""
store the whole subarrays in the node
#see https://www.youtube.com/watch?v=-UPIhagahHQ&list=PL2q4fbVm1Ik6v2-emg_JGcC9v2v2YTbvq&index=12
"""



n=8
aa=[1,4,3,5,6,4,3,2]
tree=[[] for i in range(4*n)]
def build(idx,l,r):
    if l==r:
        tree[idx].append(aa[l])
    # else:
    #     mid=(l+r)//2
    #     build(2*idx,l,mid)
    #     build(2*idx+1,mid+1,r)
    #     tree[idx]=merge(tree[2*idx],tree[2*idx+1])

    else:
        mid=(l+r)//2
        build(2*idx+1,l,mid)          # +1 for idx argument here
        build(2*idx+2,mid+1,r)        # +2 instead of +1 here
        tree[idx]=merge(tree[2*idx+1],tree[2*idx+2])  # also update the indexes used here



def merge(left,right):
    node_list=[]
    i=0
    j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:

            node_list.append(left[i])

            i += 1
        else:
            node_list.append(right[j])
            j += 1



    while i < len(left):
        node_list.append(left[i])
        i += 1


    while j < len(right):
        node_list.append(right[j])
        j += 1

    return node_list


if __name__ == '__main__':
    build(0,0,n-1)
    print(tree)