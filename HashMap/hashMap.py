'''
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
'''
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
