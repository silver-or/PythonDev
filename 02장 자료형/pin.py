# 주민번호(13자리)를 입력받아 출생년도와 나이, 성별을 출력해주는 프로그램을 작성하시오.

# 사용자 입력받기
pin = input("주민번호 13자리를 입력해주세요 : ")

# 생년월일 추출
yymmdd = pin[ : 6]

# 성별
gender = pin[6]

# 출생 연도
year = ""

# 나이
age = 0

if gender in "12" :
    year = '19' + yymmdd[ : 2]
elif gender in "34":
    year = '20' + yymmdd[ : 2]

age = 2022 - int(year) + 1

print("당신의 출생 연도는 {}년".format(year))
print("당신의 나이는 {}세".format(age))

if int(gender) % 2 == 0 :
    print("여성입니다.")
else :
    print("남성입니다.")