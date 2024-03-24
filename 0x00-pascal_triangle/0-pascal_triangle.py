#!/usr/bin/python3
"""Creating pascal triangle"""

def pascal_triangle(n):
  """This function creates a pascal trinagle based on the provided number of rows provided"""
  if n <= 0:
    return []
  
  try:
    pas_triangle = [[1]]
    
    for _ in range(1, n):
      row = [1]
      
      for i in range(1, len(pas_triangle[-1])):
        value = pas_triangle[-1][i -1] + pas_triangle[-1][i]
        row.append(value)
      row.append(1)
      pas_triangle.append(row)
    return pas_triangle
  except Exception as e:
    print("An error occurred:", str(e))
    return []

