def solution(nums):
    answer = 0
    po_dic = {}
    for num in nums:
        if num in po_dic:
            po_dic[num] += 1
        else:
            po_dic[num] = 1
    po_kind = list(po_dic.keys())
    
    if len(po_kind) <= len(nums)//2:
        return len(po_kind)
    else:
        return len(nums)//2
