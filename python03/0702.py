class Person:
    def __init__(self, name, age, address):
        self.hello = "안녕"
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))

    def getAge(self):
        print('나는 {0} 이고 나이는 {1}입니다.'.format(self.name, self.age))


james = Person('제임스', 22, '제주도')
bon = Person('본', 34, '뉴욕시')

james.greeting()

bon.greeting()
bon.age = 55

bon.getAge()


