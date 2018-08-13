import pandas as pd

# 키, 몸무게, 유형 데이트 프레임 생성하기
tbl = pd.DataFrame({"weight":[80.0,70.4,65.5,45.9,51.2,72.5],
                    "height":[170, 180, 155, 143, 154, 160],
                    "gender":["f","m","m","f","f","m"]})

# 몸무게 목록 추출하기
#print("몸무게 목록")
#print(tbl["weight"])
#print("tbl[2:4]\n", tbl[2:4])

#print("")

# 몸무게와 키 목록 추출하기
#print("몸무게와 키 목록")
#print(tbl[["weight","height"]])
#print("tbl[3:]\n", tbl[3:])


print("--- height가 이상인것")
print(tbl[tbl.height >= 160])
print("")
print("--- gender가 m 인 것")
print(tbl[tbl.gender == "m"])
print("")
print("--- 키로 정렬")  # 오름차순
print(tbl.sort_values(by="height"))
print("")
print("--- 몸무게로 정렬") # 내림차순
print(tbl.sort_values(by="weight", ascending=False))

