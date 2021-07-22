# persona_data = ['홍길동', 15, '대구광역시']
#
#
# # def personal_info(*args):
# #     for arg in args:
# #         print(arg)
#
# def personal_info(name, age, adress):
#     print(name)
#     print(age)
#     print(adress)
#
# # print(personal_info(*persona_data))
# # personal_info(age=20, adress='서울', name='강감찬')
# personal_info('강감찬', 14, adress='제주')
#
#

x = 10
print(f'전역 {x}')  # 10

def foo():
    print(f'foo() 전역 {x}')
    y = 20
    def koo():
        nonlocal y
        y = 30
        global x
        x = 40
        print(x)

    koo()
    print(y)

foo()
print(x)