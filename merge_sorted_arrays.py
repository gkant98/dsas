def merge(nums1, m, nums2, n):
    num1_copy = nums1[:m]
    p1 = 0
    p2 = 0
    for i in range(m+n):
        if p2>=n or (p1<m and num1_copy[p1]<=nums2[p2]):
            nums1[i] = num1_copy[p1]
            p1+=1
        else:
            nums1[i] = nums2[p2]
            p2+=1

def backmerge(nums1,m,nums2,n):
    p1 = m-1
    p2 = n-1
    for i in range(m+n-1,-1,-1):
        print(i,p1,p2, nums1)
        if p2<0: #This is an edge case if the second list is empty
            print('Not executing anything')
            break
        if p1>=0 and nums1[p1]>=nums2[p2]:
            nums1[i] = nums1[p1]
            p1-=1
        elif p2>=0:
            nums1[i] = nums2[p2]
            p2-=1
            
if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1,m,nums2,n)
    print(nums1)