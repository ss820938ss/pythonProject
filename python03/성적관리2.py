import json
import pickle as pi

def Search(student):
    search_name = input('검색할 친구의 이름을 입력해주세요 : ')
    if (search_name in student) == True:
        ViewHeadLine()
        print('|', search_name, end='|')
        for data in student.get(search_name):
            print(f'{data:^10}', end='|')
        print()
        ViewFootLine()
    else:
        print('해당 이름이 없습니다.')

    return  student

def Update(student):
    update_name = input('수정할 친구의 이름을 입력해주세요 : ')
    if (update_name in student) == True:
        address = input('주소을 입력하세요 : >> ')
        age = int(input('나이를 입력하세요 : >> '))
        student[update_name] = [address, age]
        person = student[update_name]
    else:
        print('해당 이름이 없습니다.')

    View(student)

def Delete(student):
    delete_name = input('삭제할 학생의 이름을 입력해주세요 : ')
    if (delete_name in student) == True:
        student.pop(delete_name)

    return student

def ViewHeadLine():
    print("=======================================================")
    print('|    이름   |           주 소         |   나이          |')

def ViewFootLine():
    print("=======================================================")

def View(student):
    ViewHeadLine()
    for key, value in student.items():
        print('|', f'{key:^6}', '|', end=' ')
        for data in value:
            print(f'{data:^20}' , end='|')
        print()
    ViewFootLine()
    return student


def Insert(student):
    name = input('이름 입력 :>> ')
    if (name not in student) == True:
        address = input('주소을 입력하세요 : >> ')
        age = int(input('나이를 입력하세요 : >>'))
        print('주소 정보가 입력되었습니다.')
    else:
        print('학생이 존재합니다.')
        return Insert(student)

    student[name] = [address, age]
    person = student[name]

    return student


def Save(student):
    with open("data.pkl", "wb") as file:
        pi.dump(student, file)  # 인코디
        print("파일이 정상적으로 저장 되었습니다.")

def mainMennu():
    print()
    print("┌---------------------------------------------------------------------------┐");
    print("│                  주소록 관리 프로그램 Ver 0.1                                │");
    print("│      1. 등록                   4. 삭제           7. 저장                    │");
    print("│      2. 목록                   5. 검색           8. json으로 저장          │");
    print("│      3. 수정                   6. 종류                                     │");
    print("└---------------------------------------------------------------------------┘\n");
    print()

def dataLoad(student):
    import os.path
    isFile = os.path.isfile('data.pkl')
    if isFile == False:
        with open("data.pkl", "wb") as file:
            print("파일을 생성 했습니다.")
            pi.dump(student, file)  # 인코디
    else:
        with open("data.pkl", "rb+") as file:
            student = pi.load(file)  # 디코더
    return student

def JsonSave(student):
    pass

def JsonLoad(jsonfilename):
    pass


def main():
    mainMennu()
    student = dict()
    student = dataLoad(student)

    while True:
        select = int(input("1.등록 2.목록 3.수정 4.삭제 5.검색 6.종료 \n"))
        if select == 1:
            student = Insert(student)
            print(student)

        elif select == 2:
            student = View(student)

        elif select == 3:
            student = Update(student)

        elif select == 4:
            student = Delete(student)
            View(student)

        elif select == 5:
            student = Search(student)

        elif select == 7:
            student = Save(student)

        elif select == 8:
            student = JsonSave(student)

        elif select == 9:
            student = JsonLoad("jsondata.json")

        else:
            break

if __name__ == "__main__":
	main()