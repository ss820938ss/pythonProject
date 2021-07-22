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


class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def getGreeting(self):
        return self.hello

    def setGreeting(self, newgreeting):
        self.hello = newgreeting

    def setWallet(self, wallet):
        self.__wallet -= wallet

    def getWallet(self):
        return self.__wallet

    def printName(self):
        return self.name

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요'.format(self.__wallet))

maria = Person('마리아', 20, '서울시', 1030303000000)
maria.pay(3000)
