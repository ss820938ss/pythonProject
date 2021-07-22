# dir([1, 2, 3])
#
# [1, 2, 3].__iter__()
#
#
# class A:
#     def __init__(self):
#         print("dddd")
#
#
# it = [1, 2, 3, 4].__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
#
# print('hello, world!'.__iter__())
# print({'a': 1, 'b': 2}.__iter__())
# print({1, 2, 3}.__iter__())
#
# str = 'hello, world!'.__iter__()
# print(str.__next__())
# print(str.__next__())
# print(str.__next__())
# print(str.__next__())
# print(str.__next__())
# print()
#
# dict_a = {'a': 'aaaa', 'b': 'bbbbb'}.__iter__()
# print(dict_a.__next__())
# print(dict_a.__next__())
# print()
#
# print(range(3).__iter__())
#
#
# class Counter:
#     def __init__(self, stop):
#         self.stop = stop
#
#     def __getitem__(self, item):
#         if item < self.stop:
#             return item
#
#         else:
#             raise IndexError
#
#
# print(Counter(3)[0])
# print()
#
# it = iter([10, 20, 30])
# print(next(it))
# print(next(it))
# print(next(it))
# print()
#
#
# import random
#
# it = iter(lambda: random.randint(0, 5), 2)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print()
#
#
# def g_number():
#     yield 0
#     yield 1
#     yield 2
#
#
# x = 1
# print(dir(x))
# g = g_number()
# print(dir(g))
#
# for i in g_number():
#     print(i)
# print("---")
#
# x = 1
# g = g_number()
#
# gg = iter(g)
# print(next(gg))
# print(next(gg))
# print("---")



