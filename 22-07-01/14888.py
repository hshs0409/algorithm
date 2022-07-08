# https://www.acmicpc.net/problem/14888

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9


def dfs(count, res, add, sub, mul, div):
    global max_, min_
    if count == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(count + 1, res + nums[count], add - 1, sub, mul, div)
        if sub:
            dfs(count + 1, res - nums[count], add, sub - 1, mul, div)
        if mul:
            dfs(count + 1, res * nums[count], add, sub, mul - 1, div)
        if div:
            dfs(count + 1, int(res / nums[count]), add, sub, mul, div - 1)


dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)
