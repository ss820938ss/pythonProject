from abc import *

# class Person:
#     bag = []  # 클래스변수

# bag_class = []

# def __init__(self, name):
#     self.name = name  # 인스턴스 변수

# def put_bag(self, stuff):
#     self.bag.append(stuff)

# def put_bag(self, stuff):
#     Person.bag.append(stuff)


# james = Person("제임스")
# james.put_bag("책")
#
# maria = Person("마리아")
# maria.put_bag("열쇠")

# print(james.bag)
# print(james.name)
# print(maria.bag)
# print(maria.name)

# print(Person.bag.append("ddddd"))
# print(Person.bag)
#
# james = Person()
# james.bag.append("cccccccccccccc")
# print(james.__dict__)
# print(Person.__dict__)


###

# def sub(a, b):
#     print(a - b)


# class Calc:
#     @staticmethod
#     def add(a, b):
#         print(a + b)
#
#     @staticmethod
#     def mul(a, b):
#         print(a * b)
#
#
# Calc.add(10, 20)
# Calc.mul(10, 20)
#
# cc = Calc()
# sub(10, 20)


###


#     def add(cls, a):
#         cls.count += a
#         print(cls.count)
#
#
# Person.print_count()


# class Person:
#     count = 0
#
#     def __init__(self):
#         Person.count += 1
#
#     @classmethod
#     def print_count(cls):
#         print("{0} 개의 객체가 생성 되었습니다.".format(cls.count))
#
#
# Person.count = 10
# james = Person()
# maria = Person()
#
# Person.print_count()
# print(Person.count)


###
#
# class Counter:
#     def __init__(self, value=0):
#         self.value = value
#
#     def increment(self, delta=1):
#         self.value += delta
#
#     def decrement(self, delta=1):
#         self.value -= delta
#
# cc = Counter()
# cc.value
#
# dd = Counter()
# dd.value

###

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def fromTuple(cls, tup):
        return cls(tup[0], tup[1])

    @classmethod
    def fromDictionary(cls, dic):
        return cls(dic["email"], dic["password"])


abc = User('aa@a.com', '1111')
print(abc.email, abc.password)

user = User.fromTuple(("user@test.com", "1234"))
print(user.email)
print(user.password)


###

class StringUtils:
    @staticmethod
    def toCamelcase(text):
        words = iter(text.split("_"))
        return next(words) + "".join(i.title() for i in words)

    @staticmethod
    def toSnakecase(text):
        letters = ["_" + i.lower() if i.isupper() else i for i in text]
        return "".join(letters).lstrip("_")


print(StringUtils.toCamelcase("abc_dae_de"))


###

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("안녕하세요")


# class Person_list():
#     def __init__(self):
#         self.person_list = []
#
#     def append_person(self, person):
#         self.person_list.append(person)
#
# pl = Person_list()
# gildong = Person("홍길동")
# gangchan = Person("강감찬")
#
# pl.append_person(gildong)
# pl.append_person(gangchan)
#
# pl.person_list[0].greeting()
# print(pl.person_list[0].name)


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greeting(self):
#         print("안녕하세요.")
#
#
# class Student(Person):
#     def __init__(self, person):
#         self.person = person
#
#     def study(self):
#         print("공부합니다.")
#
#
# class Policeman(Person):
#     def __init__(self, num):
#         self.gun = Gun(num)
#
#     def exp(self):
#         print("근무합니다")
#
#
# class Gun():
#     def __init__(self, num):
#         self.num = num
#
#     def shooting(self):
#         print("권총 발사")
#
#
# po = Policeman("이순신")
# print(po.__dict__)
#
#
# po = Policeman("이은정")
# # po.name = "aaaa"
# print(po.__dict__)
# print()
#
# st = Student("홍길동")
# print(st.__dict__)
# st.greeting()
# st.study()

###
#
# class Person():
#     def greeting(self):
#         print("안녕하세요.")
#
#
# class University():
#     def manage_credit(self):
#         print("학점관리")
#
#
# class Undergraduate(Person, University):
#     def study(self):
#         print("공부하기")
#
#
# ug = Undergraduate()
# ug.study()
# ug.greeting()


###

class Human(metaclass=ABCMeta):
    # 추상 메서드
    @abstractmethod
    def walk(self):
        print('Human walk : 사람은 걸어요')

    # 추상 메서드
    @abstractmethod
    def talk(self):
        pass

    # 일반 메서드
    def sleep(self):
        print('Human sleep : 사람은 자요')


# 자식 클래스 : 어른 클래스
class Adult(Human):
    def walk(self):
        print('Adult walk : 어른은 걷습니다.')


# 자식 클래스 : 아기 클래스
class Baby(Human):
    # 추상 메서드
    def walk(self):
        print('Baby walk : 아기는 기어갑니다.')

    def talk(self):
        print('Baby talk : 아기는 옹알이를 합니다.')


# 객체 생성
# human = Human() # error
# adult = Adult() # error
baby = Baby()

# 재정의한 추상 메서드
baby.walk()
baby.talk()

# 부모 클래스 메서드
baby.sleep()
