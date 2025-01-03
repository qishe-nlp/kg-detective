def merge_range(first, second):
  """Merge two tuples, which have two elements respectively 

  Args:
    first (tuple): (start, end)
    second (tuple): (start, end)

  Returns:
    list: merged tuples


  Examples:
    >>> merge_range((1, 3), (4, 8))
    [(1, 3), (4, 8)]

    >>> merge_range((1, 3), (3, 8))
    [(1, 3), (3, 8)]

    >>> merge_range((1, 3), (2, 8))
    [(1, 8)]
  """

  if first[1] <= second[0] or first[0] >= second[1]:
    return [first, second]
  else:
    return [(min(first[0], second[0]), max(first[1], second[1]), first[2])]


def merge(ranges):
  """Merge a list of tuples, which have two elements respectively 

  Args:
    ranges (list): [(start1, end1), (start2, end2), ...]

  Returns:
    list: merged tuples


  Examples:
    >>> merge([(1, 4),(3, 6), (4, 7), (9, 12)])
    [(1, 7), (9, 12)]
  """

  if len(ranges) == 0:
    return []
  ordered = sorted(ranges, key=lambda pair: pair[0])
  result = [ordered[0]] 
  for e in ordered[1:]:
    merged = merge_range(result[-1], e)
    del result[-1]
    result.extend(merged)
  return result



def refine(matches):
  """Make order of a list of lists of tuples, which have four elements

  Args:
    matches (list): [(s1, e1, m1, gid1), (s2, e2, m2, gid1), (s3, e3, m3, gid2), ...]

  Returns:
    list: tuples

  Examples:
    >>> refine([(1, 4, 'm1', 1), (8, 10, 'm2', 1), (5, 6, 'n1', 2), (12, 14, 'n2', 2)])
    [(1, 4, 'm1', 1), (5, 6, 'n1', 2), (8, 10, 'm2', 1), (12, 14, 'n2', 2)]
  """
  
  if len(matches) == 0:
    return []

  ordered = sorted(matches, key=lambda p: p[0])
  return ordered












