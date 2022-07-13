'''
Problem 1: 
Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933

hashMap = {}
num = int(input())
for i in range(num):
    string, phoneNum = input().split()
    hashMap[string] = int(phoneNum)
# print(hashMap)
for i in range(num):
    string = input()
    if string in hashMap:
        print("{}={}".format(string, hashMap[string]))
    else:
        print('Not found')
--------
Problem 2: Check the duplicate element => Return true if not, otherwise not
Approach: Traver through all elements in the array 
Assign the number of time it appears on List

hashMap = {}
nums = [1,2,3,4,5]
for value in nums:
    if value in hashMap:
        print("True")
    else:
        hashMap[value] = 1
        print(hashMap[value])
----
Problem 3: Contains Duplicate II
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true

'''
hashMap = {}
nums= [1, 2, 3, 1]
k = 3
for key, value in enumerate(nums):
    if value in hashMap and key - hashMap[value] <= k:
        print(value)
    hashMap[value] = key
print(hashMap)