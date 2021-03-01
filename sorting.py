import time

def selection_sort(arr):
  '''
  O(n^2), space=O(1)
  Repeatedly finding the minimum element (considering ascending order) from
  unsorted part and putting it at the beginning.
  In every iteration of selection sort, the minimum element (considering
  ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
  '''

  for i in range(len(arr)): # len -1 ?
    min_idx = i # Init with current

    #iterate over the rest of the array to compar
    for j in range(i+1, len(arr)):
      if(arr[j] < arr[min_idx]):
        min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

  return arr

def bubble_sort(arr):
  '''
  O(n^2), space=O(1)
  Traverse through the array. In the inner pass, traverse through the
  subarray from the start till the end - minus current index.
  Two pass - swap consecutive numbers if left > right.
  '''
  n = len(arr) # 5
  for i in range(n): # 0
    for j in range(0, n - i - 1): #4
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

def insertion_sort(arr):
  '''
  O(n^2), space=O(1)
  Traverse through the arr: If current key < prev, check with keys before
  that and push to an ordered position.
  '''

  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >=0 and key < arr[j]: # Reverse traversal
      arr[j + 1] = arr[j] # Shift all to the right
      j -= 1
    arr[j+1] = key

  return arr

def merge_sort(arr):
  '''
  O(nlogn), space=O(n)
  Applications: Merge Linked Lists, Inversion Count
  Divide and conquer. Find midpoint,use as a pivot to slice the array
  into left and right and sort left and right separately. Merge them
  later.
  '''

  if len(arr) > 1:
    # Find midpoint
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    i = j = k = 0

    # Merge the lists
    while i < len(left_arr) and j < len(left_arr):
      if left_arr[i] < right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j = 1
      k += 1

    # Add the remnant
    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1

    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1

  return arr

def quick_sort(arr):
  '''
  O(nlogn), space-o(n)
  Find partition - use the last number
  Choose the pivot - iterate through and place smaller<pivot in one array
  larger>pivot in the other array.
  Sort the subarrays using the same implementation
  Merge recursively - less + pivot + greater
  '''
  length = len(arr)
  if length <= 1:
    return arr
  pivot = arr.pop() # removing the last element as pivot

  items_lesser = []
  items_greater = []

  for item in arr:
    if item > pivot:
      items_greater.append(item)
    else:
      items_lesser.append(item)


  return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)


if __name__ == '__main__':
  arr = [64, 25, 12, 22, 11, 50, 14, 1004,
         222, 9, 19, 56, 90, 189, 506, 79, 851,
         921, 1, 5, 100, 89, 99, 354, 979,
         29, 38, 62, 912, 123, 7]

  print("SELECTION SORT")
  print(selection_sort(arr))
  print("BUBBLE SORT")
  print(bubble_sort(arr))
  print("INSERTION SORT")
  print(insertion_sort(arr))
  print("MERGE SORT")
  print(merge_sort(arr))
  print("QUICK SORT")
  print(quick_sort(arr))
