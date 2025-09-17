# # bubble sort
# def bubble_sort_visual(arr):
#     n = len(arr)
#     print(f"Original list: {arr}")
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         print(f"sort{i+1}: {arr}")
#         if not swapped:
#             break
# arr = [5, 3, 8, 4, 2]
# bubble_sort_visual(arr)

# selection sort
# def selection(arr):
#     n = len(arr)
#     print("Original array:", arr)
#     for i in range(n):
#         minimum = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[minimum]:
#                 minimum = j
#         if minimum != i:
#             arr[i], arr[minimum] = arr[minimum], arr[i]
#             print(f"Step {i + 1}: {arr}")
#         else:
#             print(f"Step {i + 1}: {arr}")
#         if arr[i:] == sorted(arr[i:]):
#             break
#     return arr
#
# data = [29, 10, 14, 37, 13]
# sorted_data = selection(data)

#Merge sort
