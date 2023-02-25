def spy_game(nums):
    str = ""
    for x in nums:
        if x == '0' or x == '7':
            str += x
        else:
            continue
    if str == "007":
        print(True)
    else:
        print(False)
nums = list(input().split())
spy_game(nums)