def total(numbers):
    sum_so_far = 0
    for number in numbers:
        sum_so_far += number
    return sum_so_far

print total([1, 2, 3])
print total([7, -4, 1, 6, 0])
print total([])

