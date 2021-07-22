def PointPrint():
    print('p1: {} {}'.format(p1.x, p1.y))


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)

print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))


# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point2D(x=30, y=20)
# p2 = Point2D(x=60, y=50)
#
# a = p2.getX() - p1.getX()
# b = p2.getY() - p1.getY()
# c = math.sqrt((a*a) + (b*b))
# print(c)


##


class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)


three_multiple()

