import math


def get_square_roots(number):
  """
  The function takes a number and returns a list of the square roots of that number.
  """
  if number < 0:
    return []
  elif number == 0:
    return [number]
  return [-(math.sqrt(number)), (math.sqrt(number))]


def get_range(n):
  """
  For a given positive number of the argument n, the function returns a list of numbers from zero to n, excluding the number n itself. For negative value and 0 returns an empty list.
  """
  range_of_numbers = []
  if n <= 0:
    return range_of_numbers
  i = 0
  while i < n:
    range_of_numbers.append(i)
    i += 1
  return range_of_numbers 