"""Reverse Array"""
# arr = [10, 20, 30, 40, 50]
# reversed_arr = arr[::-1]
# print(reversed_arr)


"""Reverse Array using loop"""
# num = [1, 2, 3, 4, 5]
# reversed_arr = []
# for i in range(len(num)-1, -1, -1):
#     reversed_arr.append(num[i])
# print(reversed_arr)    


"""Swap Logic(Using temperory variable)"""
# a = 10
# b = 20
# temp = a
# a = b 
# b = temp

# print(a, b)


"""Swap Logic (Python shortcut)"""
# a = 10
# b = 20
# a, b = b, a
# print(a, b)


"""Two Pointer"""
# arr = [10, 20, 30, 40, 50]
# left = 0
# right = len(arr) - 1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)    


"""Duplicate (Using Loop[Brute Force])"""
# arr = [10, 20, 30, 20]
# duplicate = False
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j]:
#             duplicate = True
# print(duplicate)            


"""Set"""
# num = {10, 20, 30, 20}
# print(num)


"""Using Set Automatically Remove Duplicate(Optimized)"""
# arr = [10, 20, 30, 20]
# if len(arr) != len(set(arr)):
#     print("Duplicate Found")
# else:
#     print("No Duplicate")    


"""Another optimized method"""
# arr = [10, 20, 30, 20]
# seen = set()
# for num in arr:
#     if num in seen:
#         print("Duplicate Found")
#         break

#     seen.add(num)










"""Reverse List"""
# arr = [1, 2, 3, 4, 5]
# left = 0
# right = len(arr) - 1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)    


"""Duplicate Detection Using Set"""
# arr = [1, 2, 3, 2]
# seen = set()
# for num in arr:
#     if num in seen:
#         print("Duplicate Found")
#         break
#     seen.add(num)


"""Remove Duplicates"""
# arr = [1, 2, 2, 3, 3, 4]
# result = list(set(arr))
# print(result)

"""Find First Duplicate"""
# arr = [5, 2, 1, 5, 3]
# seen = set()
# for num in arr:
#     if num in seen:
#         print(num)
#         break
#     seen.add(num)






