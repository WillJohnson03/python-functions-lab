def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

# print(sum_to(6))
# print(sum_to(10))

def largest(nums):
  nums.sort()
  return nums[-1]

# print(largest([1, 2, 3, 4, 0]))
# print(largest([10, 4, 2, 231, 91, 54]))

def occurrences(string, substr):
  return string.count(substr)

# print(occurrences('fleep floop', 'e'))
# print(occurrences('fleep floop', 'p'))
# print(occurrences('fleep floop', 'ee'))
# print(occurrences('fleep floop', 'fe'))

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(-1, 4))
# print(product(2, 5, 5))
# print(product(4, 0.5, 5))