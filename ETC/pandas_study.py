import pandas as pd

# pandas는 시리즈(Series), 데이터프레임(DataFrame), 패널(Panel) 3가지의 데이터 구조를 가짐
# 시리즈는 1차원 배열의 값에 대응되는 인덱스를 부여할 수 있음

# sr = pd.Series([1, 2, 3, 4], index=["하나", "둘", "셋", "넷"])
# print(sr)
# print(sr.values)
# print(sr.index)


# 데이터프레임은 2차원 리스트를 매개변수로 전달하여 행과 열, 값으로 구성됨
# values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# index = ["하나", "둘", "셋"]
# columns = ["A", "B", "C"]
#
# df = pd.DataFrame(values, index=index, columns=columns)
#
# print(df)
# print(df.index)
# print(df.columns)
# print(df.values)



# Ex
data = [["1000", "kim", 80], ["1001", "jo", 85], ["1002", "mo", 70],
        ["1003", "lee", 90], ["1004", "park", 100], ["1005", "hong", 90]]
#
# df1 = pd.DataFrame(data)
# print(df1)
#
# print("====================")
#
#
# 인덱스와 열 이름을 지정해서 생성
# df2 = pd.DataFrame(data, columns=["학번", "이름", "점수"], index=[1, 2, 3, 4, 5, 6])
# print(df2)
#
# print("====================")
#
# print(df2.head(2))   # 앞 부분 2개 출력
# print("====================")
# print(df2.tail(2))   # 뒷 부분 2개 출력
# print("====================")
# print(df2["학번"])   # 학번에 해당하는 열만 출력


# 인덱스, 열 이름 바꾸기 및 삭제
# df2 = pd.DataFrame(data, columns=["학번", "이름", "점수"], index=["1", "2", "3", "4", "5", "6"])
#
# print(df2)
# df2.columns = ["학번1", "이름1", "점수1"]   # 열 이름 바꾸기
# print("====================")
# print(df2)
# print("====================")
# df2.index = ["10", "20", "30", "40", "50", "60"]   # 인덱스 이름 바꾸기
# print(df2)
# print("====================")
# df2.drop("10", inplace=True)   # 인덱스가 10인 행 삭제, drop()은 원본 객체를 변경하지 않기 때문에 inplace=True 추가해야함
# print(df2)
# print("====================")
# df2.drop(["학번1", "이름1"], axis=1, inplace=True)   # 학번1과 이름1 열을 삭제
# print(df2)


# 행 선택(loc, iloc) 및 열 선택
df3 = pd.DataFrame(data, columns=["학번", "이름", "점수"], index=["1", "2", "3", "4", "5", "6"])

# 인덱스 이름을 기준으로 행을 선택할때는 loc
# 정수형 위치 인덱스를 사용할때는 iloc
# print(df3)
# print("====================")
# print(df3.loc["3"])
# print("====================")
# print(df3.loc[["3", "4"]])
# print("====================")
# print(df3.iloc[2])
# print("====================")
# print(df3.iloc[[2, 4]])
# print("====================")
# print(df3["학번"])   # 학번 열 출력
# print("====================")
# print(df3[["학번", "이름"]])   # 학번, 이름 열 출력


# read_csv, to_csv
df4 = pd.read_csv("dataset/test_csv_file.csv")
print(df4)
# 옵션중 sep는 구분자로 콤마로 구분된 것이 아니라면 "|"이나 "\t"를 전달해야함
# read_csv()는 기본적으로 첫번째 행을 header(열 이름)로 지정하지만 header가 없을 경우 header=None을 지정해야함

# 특정한 열을 인덱스로 지정할때
df5 = pd.read_csv("dataset/test_csv_file.csv", index_col="AGE")
df6 = pd.read_csv("dataset/test_csv_file.csv", index_col=2)
print(df6)

# 열 이름을 변경할 때
df7 = pd.read_csv("dataset/test_csv_file.csv", names=["qq", "ww", "ee"])
print(df7)

# 특정 값을 NaN으로 변경할 때
df8 = pd.read_csv("dataset/test_csv_file.csv", na_values=["30"])
print(df8)











