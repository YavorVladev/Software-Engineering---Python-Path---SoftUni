from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    result = ""
    while nums:
        kwargs['a'] += nums.popleft()
        if not nums:
            break
        kwargs['s'] -= nums.popleft()
        if not nums:
            break
        divisor = nums.popleft()
        if divisor != 0:
            kwargs['d'] /= divisor
        if not nums:
            break
        kwargs['m'] *= nums.popleft()
        if not nums:
            break
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for value in sorted_dict:
        result += f"{value[0]}: {value[1]:.1f}" + '\n'

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
