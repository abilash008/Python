
k = [1,
     2,
     3,
     4,
     [22,33,44,[3,4,5,'python'],21,22,23,[10,20,30,4],45,56,78,89],
     41,
     52,
     63,
     'abhilash',
     ['irfan','diwakar','xyz','ABC'],
     50,
     20]
print(len(k))
# print(k[:])
# [1, 2, 3, 4, [22, 33, 44, [3, 4, 5, 'python'], 21, 22, 23, [10, 20, 30, 4], 45, 56, 78, 89],
# 41, 52, 63, 'abhilash', ['irfan', 'diwakar', 'xyz', 'ABC'], 50, 20]

# print(k[5][3][2])
# TypeError: 'int' object is not subscriptable
print(k[4][3][2])
# 5

