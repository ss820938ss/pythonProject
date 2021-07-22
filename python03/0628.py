# a = [10, 20, 30, 40, 50]
# print(id(a))
#
#
# def minfind(ma):
#     print(id(ma))
#     smallest = ma[0]
#     for value in ma:
#         if value < smallest:
#             smallest = value
#     print(smallest)
#
#
# def maxfind(ma):
#     print(id(ma))
#     a[2] = 100
#     smallest = ma[0]
#     for value in ma:
#         if value > smallest:
#             smallest = value
#     print(smallest)
#
#
# a = [[10, 20], [30, 40], [50, 60]]
# for b, c in a:
#     print(b, c)



# test
# for 문 이용해서 가로 6 세로 6의 배열의 가로세로 합을 구하기

# a = [[0 for b in range(1)] for c in range(6)]
# print(a)

# a = [6, 6, 6, 6, 6, 6]
# b = []
#
# for i in a:
#     line = []
#     for j in range(i):
#         line.append(0)
#     b.append(line)
#
# print(b)


# a = [[ 1,  2,  3,  4,  5,  6],
#      [ 7,  8,  9, 10, 11, 12],
#      [13, 14, 15, 16, 17, 18],
#      [19, 20, 21, 22, 23, 24],
#      [25, 26, 27, 28, 29, 30],
#      [31, 32, 33, 34, 35, 36]]
# for b, c, d, e, f, g in a:
#
#     print(b, c, d, e, f, g)




#  a = [
#       [1, 2, 3, 4, 5, 6],
#       [7, 8, 9, 10, 11, 12],
#       [13, 14, 15, 16, 17, 18],
#       [19, 20, 21, 22, 23, 24],
#       [25, 26, 27, 28, 29, 30],
#       [31, 32, 33, 34, 35, 36]
#       ]
# # result = []
# # for num in a:
# #     result.append(num*3)
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()


# a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]

# for i in range(len(a)):  # 세로 크기
#     for j in range(len(a[i])):  # 가로 크기
#         print(a[i][j], end=' ')
#     print()

# a = [[10, 20], [30, 40], [50, 60]]

# i = 0
# while i < len(a):
#     b, c, d, e, f, g = a[i]
#     print(b, c, d, e, f, g)
#     i += 1
#     print()
#
# print(sum(a[0]))  # 가로합
# print(sum(a[1]))  # 가로합
# print(sum(a[2]))  # 가로합
# print(sum(a[3]))  # 가로합
# print(sum(a[4]))  # 가로합
# print(sum(a[5]))  # 가로합


a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
for i in range(0, 5):
  for j in range(0, 5):
    if j < 7:
      a[i][5] += a[i][j]
    else:
      a[i][5] = a[i][3]/6
    print(a[i][j], end = "\t")
  print()






