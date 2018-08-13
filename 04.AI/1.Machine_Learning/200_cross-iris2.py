import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re
# 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
csv = pd.read_csv('iris.csv')
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기 --- (※2)
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]
# 크로스 밸리데이션하기 --- (※3)
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())
# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (1)
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:,0:1]    # 데이터
xor_label = xor_df.ix[:,2]     # 레이블

# 데이터 학습과 예측하기 --- (2)
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기 --- (3)
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", ac_score)