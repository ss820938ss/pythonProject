# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title("test")
# root.geometry("600x400+100+100")
# root.resizable(False, False)
#
#
# def show():
#     print("item1: %d,\nitem2: %d,\nitem3: %d\n" % (variety1.get(), variety2.get(), variety3.get()))
#     messagebox.showinfo("Button Clicked",
#                         "item1: {0},\nitem2: {1},\nitem3: {2}\n".format(variety1.get(), variety2.get(), variety3.get()))
#
#
# def selectall():
#     bt1.select()
#     bt2.select()
#     bt3.select()
#
#
# def deselectall():
#     bt1.deselect()
#     bt2.deselect()
#     bt3.deselect()
#
#
# variety1 = IntVar()
# variety2 = IntVar()
# variety3 = IntVar()
#
# bt1 = Checkbutton(root, text="item1", variable=variety1)
# bt2 = Checkbutton(root, text="item2", variable=variety2)
# bt3 = Checkbutton(root, text="item3", variable=variety3)
#
# bt1.pack()
# bt2.pack()
# bt3.pack()
#
# buttonSelectAll = Button(root, width=10, text="전체선택", overrelief="solid", command=selectall)
# buttonSelectAll.pack()
#
# buttonDeSelectAll = Button(root, width=10, text="전체취소", overrelief="solid", command=deselectall)
# buttonDeSelectAll.pack()
#
# button = Button(root, width=10, text="Show", overrelief="solid", command=show)
# button.pack()
#
# root.mainloop()


# import numpy as np, cv2
#
# image1 = np.zeros((300, 300), np.uint8)     		# 300행, 300열 검은색 영상 생성
# image2 = image1.copy()
#
# h, w = image1.shape[:2]
# cx,cy  = w//2, h//2
# cv2.circle(image1, (cx,cy), 100, 255, -1)      		# 중심에 원 그리기
# cv2.rectangle(image2, (0,0, cx, h), 255, -1)
#
# image3 = cv2.bitwise_or(image1, image2)     	# 원소 간 논리합
# image4 = cv2.bitwise_and(image1, image2)    	# 원소 간 논리곱
# image5 = cv2.bitwise_xor(image1, image2)    	# 원소 간 배타적 논리합
# image6 = cv2.bitwise_not(image1)            	# 행렬 반전
#
# cv2.imshow("image1", image1);			cv2.imshow("image2", image2)
# cv2.imshow("bitwise_or", image3);		cv2.imshow("bitwise_and", image4)
# cv2.imshow("bitwise_xor", image5);	cv2.imshow("bitwise_not", image6)
# cv2.waitKey(0)

# import numpy as np, cv2
#
# x = np.array([1, 2, 3, 5, 10], np.float32)            # 리스트를 numpy array로 변환
# y = np.array([2, 5, 7, 2, 9]).astype("float32")
#
# mag = cv2.magnitude(x, y)                   # 크기 계산
# ang = cv2.phase(x, y)                       # 각도(방향) 계산
# p_mag, p_ang  = cv2.cartToPolar(x, y)  # 극좌표로 변환
# x2, y2 = cv2.polarToCart(p_mag, p_ang)  # 직교좌표로 변한
#
# print("[x] 형태: %s 원소: %s" % ( x.shape, x))
# print("[mag] 형태: %s 원소: %s" % ( mag.shape, mag))
#
# print(">>>열벡터를 1행에 출력하는 방법")
# print("[m_mag] = %s" % mag.T)
# print("[p_mag] = %s" % np.ravel(p_mag))
# print("[p_ang] = %s" % np.ravel(p_ang))
# print("[x_mat2] = %s" % x2.flatten())
# print("[y_mat2] = %s" % y2.flatten())


# import numpy as np, cv2
#
# m1 = np.full((3, 6), 10, np.uint8)			# 단일 채널 생성 및 초기화
# m2 = np.full((3, 6), 50, np.uint8)
# m_mask = np.zeros(m1.shape, np.uint8)		# 마스크 생성
# m_mask[ :, 3: ] = 1							# 관심 영역을 지정한 후, 1을 할당
#
# m_add1 = cv2.add(m1, m2)                    # 행렬 덧셈
# m_add2 = cv2.add(m1, m2, mask=m_mask)       # 관심 영역만 덧셈 수행
#
# # 행렬 나눗셈 수행
# m_div1 = cv2.divide(m1, m2)
# m1 = m1.astype(np.float32)                  # 형변환 - 소수 부분 보존
# m2 = np.float32(m2)
# m_div2 = cv2.divide(m1, m2)
#
# titles = ['m1', 'm2', 'm_mask','m_add1','m_add2','m_div1', 'm_div2']
# for title in titles:
#     print("[%s] = \n%s \n" % (title, eval(title)))


# import numpy as np
# import cv2
#
# # numpy array이용해 단일 채널 3개 생성
# ch0 = np.zeros((2, 4), np.uint8) + 10           # 0원소 행렬 선언 후 10 더하기
# ch1 = np.ones((2, 4), np.uint8) * 20            # 1원소 행렬 선언 후 20 곱하기
# ch2 = np.zeros((2, 4), np.uint8); ch2[:] = 30   # 0원소 행렬 선언 후 행렬원소값 30 지정
#
# list_bgr = [ch0, ch1, ch2]                      # 단일 채널들을 모아 리스트 구성
# merge_bgr = cv2.merge(list_bgr)                 # 채널 합성
# split_bgr = cv2.split(merge_bgr)                # 채널 분리: 컬러영상--> 3채널 분리
#
# print('split_bgr 행렬 형태 ', np.array(split_bgr).shape)
# print('merge_bgr 행렬 형태', merge_bgr.shape)
#
# print("[ch0] = \n%s" % ch0)                     # 단일 채널 원소 출력
# print("[ch1] = \n%s" % ch1)
# print("[ch2] = \n%s" % ch2)
# print("[merge_bgr] = \n %s\n" % merge_bgr)       # 다중 채널 원소 출력
#
# print("[split_bgr[0]] =\n%s " % split_bgr[0])
# print("[split_bgr[1]] =\n%s " % split_bgr[1])
# print("[split_bgr[2]] =\n%s " % split_bgr[2])


# 사진뺴고 카메라영상에 로고 넣기
import numpy as np, cv2

image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo  = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None: raise Exception("영상 파일 읽기 오류 ")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]  # 로고 영상 이진화
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])       # 전경 통과 마스크
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)            # 배경 통과 마스크

(H, W), (h, w) = image.shape[:2], logo.shape[:2]                       # 로고 영상 크기
x, y = (W-w)//2, (H - h)//2
roi = image[y:y+h, x:x+w]                # 관심 영역(roi) 지정

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask) # 로고의 전경 복사
background = cv2.bitwise_and(roi , roi , mask=bg_pass_mask) # roi에 원본배경만 복사

dst = cv2.add(background, foreground)            # 로고 전경과 원본 배경 간 합성
image[y:y+h, x:x+w] = dst             # 합성 영상을 원본에 복사

cv2.imshow("background", background);  cv2.imshow("forground", foreground)
cv2.imshow("dst", dst);                 cv2.imshow("image", image)
cv2.waitKey()