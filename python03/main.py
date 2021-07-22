# print("안녕하세요")
# print("fdfdfd"); print("tlfgod")
# print("dfdfd"); print("rerrr")
#
# a = 10
# if a == 10 :
#     print("a에 10이 있네용")
#     if a > 10 :
#         print("dldldl")
# print("====================")
#
# print(1+2)
#
# quotient, remainder= divmod(5, 2)
# print(quotient, remainder)
#
# print(0b110)
#
# print("======================")
#
# x, y, z = 10, 20, 30
# print(y)
#
# t, e, d = 10, 20.4, 30
# print(type(t))
# print(type(e))
# print(type(d))

import calcpkg.operation
import calcpkg.geometry

print(calcpkg.operation.add(10, 20))
print(calcpkg.operation.mul(10, 20))

print(calcpkg.geometry.triangle_area(30, 40))
print(calcpkg.geometry.rectangle_area(30, 40))
