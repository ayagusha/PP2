def has_33(nums):
    k = len(nums)
    cnt = 0
    for x in range(k):
        if x < k - 1 :
            if nums[x] == '3' and nums[x+1] == '3':
                cnt += 1
            else:
                continue
    if cnt >= 1:
        print(True)
    else:
        print(False)
nums = list(input().split())
has_33(nums)