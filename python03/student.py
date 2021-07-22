import pickle as pi
import json


# 검색  기능추가숙제
def Search(student):
    search_name = input('검색할 이름을 입력해주세요: ')

    if (search_name in student) == True:
        ViewheadLine()
        print('||', f'{search_name:^7}', '||', end=' ')
        for data in student.get(search_name):
            print(f'{data:^11}', ' ', end='||')
        ViewfooterLine()
    else:
        print('해당 이름이 없습니다.')

    return student


# 수정
def Update(student):
    update_name = input('수정할 이름을 입력해주세요: ')
    if (update_name in student) == True:
        adress = input('주소를 입력하세요: ')
        age = int(input('나이를 입력하세요: '))
        student[update_name] = [adress, age]
        person = student[update_name]
    else:
        print('해당 이름이 없습니다.')

    View(student)
    return student


def ViewheadLine():
    print("------------------------------------------------")
    print('||    이름    ||       주소       ||    나이    ||')


def ViewfooterLine():
    print()
    print("------------------------------------------------")


# 목록
def View(student):
    for key, value in student.items():
        ViewheadLine()
        print('||', f'{key:^7}', '||', end=' ')
        for data in value:
            print(f'{data:^11}', ' ', end='||')
        print()
        ViewfooterLine()
    return student


# 등록
def Insert(student):
    name = input('이름 입력: ')
    if name not in student:
        adress = input('주소를 입력하세요: ')
        age = int(input('나이를 입력하세요: '))
        print('주소 정보가 입력되었습니다.')
    else:
        print('학생이 존재합니다.')
        return Insert(student)

    student[name] = [adress, age]
    person = student[name]

    return student


def Delete(student):
    delete_name = input('삭제할 이름을 입력해주세요 : ')
    if (delete_name in student) == True:
        student.pop(delete_name)

    return student


# 수정
def Save(student):
    with open("data.pkl", "wb") as file:
        pi.dump(student, file)  # 인코디
        print("파일이 정상적으로 저장되었습니다.")


# Json저장
def JsonSave(student):
    with open("jsondata.json", "w") as json_file:
        json.dump(student, json_file)
        print('파일이 정상적으로 저장되었습니다.')
    return student


# Json로드
def JsonLoad(student):
    with open("jsondata.json", "r") as st_json:
        st_python = json.load(st_json)
        print('파일이 정상적으로 로드되었습니다.')
    return student


def mainMenu():
    print()
    print("┌----------------------------------------------------------------------------┐");
    print("│                            <주소록 관리 프로그램>                             │");
    print("│                1. 등록              4. 수정              7. 저장             │");
    print("│                2. 목록              5. 삭제              8. json으로 저장     │");
    print("│                3. 검색              6. 종료              9. json으로 로드     │");
    print("└----------------------------------------------------------------------------┘\n");

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


def main():
    mainMenu()
    student = dict()
    student = dataLoad(student)

    while True:
        #  등록
        select = int(input("1. 등록  2. 목록  3. 검색  4. 수정  5. 삭제  6. 종료  7. 저장  8. json으로 저장  9. json으로 로드 \n"))
        if select == 1:
            student = Insert(student)
        #  목록
        elif select == 2:
            student = View(student)
        #  검색    
        elif select == 3:
            student = Search(student)
        #  수정
        elif select == 4:
            Update(student)
        #  삭제
        elif select == 5:
            student = Delete(student)
        # 파일저장
        elif select == 7:
            student = Save(student)
        # json 저장
        elif select == 8:
            JsonSave(student)
        # json 로드
        elif select == 9:
            JsonLoad("jsondata.json")
        else:
            break


if __name__ == "__main__":
    main()
