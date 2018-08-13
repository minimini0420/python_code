import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

housing_file_path = 'Housing.csv'
housing = pd.read_csv(housing_file_path)
# print(housing.columns)

housing['housing_driveway'] = np.where(housing['driveway'] == 'yse',1.,0.)
housing['housing_recroom'] = np.where(housing['recroom'] == 'yse',1.,0.)
housing['housing_fullbase'] = np.where(housing['fullbase'] == 'yse',1.,0.)
housing['housing_gashw'] = np.where(housing['gashw'] == 'yse',1.,0.)
housing['housing_airco'] = np.where(housing['airco'] == 'yse',1.,0.)
housing['housing_prefarea'] = np.where(housing['prefarea'] == 'yse',1.,0.)

# 다른 방법 replace를 활용해서
# housing = housing.replace('yes', 1)
# housing = housing.replace('no', 0)

housing_price_data = housing.price
# print(housing_price_data)

housing_price_datalist = []
housing_price_predict_list = []
i = 0
while True:
    if i != 5:  # 가격수정, 밑에 t랑 맞추거나 수정 가능하다.
        housing_price_datalist.append(housing_price_data[i])
        i= i + 1
    else:
        break

housing_predictors = ['lotsize','bedrooms','bathrms','stories','housing_driveway','housing_recroom','housing_fullbase','housing_gashw',
                      'housing_airco','garagepl','housing_prefarea']

y = housing_price_data
x = housing[housing_predictors]

housing_model = DecisionTreeRegressor()
housing_model.fit(x,y)

t = 0
while True:
    if t != 5:
        housing_price_predict_list.append(housing_model.predict(x.head())[t]) # head를 쓰면 index를 5개 까지 밖에 못가진다.
        t = t + 1                                                             # head 안에다가 숫자를 넣으면 해당 숫자만큼 늘어난다!!
    else:
        break

# print(housing_price_predict_list)

A = housing_price_datalist
B = housing_price_predict_list
result_value = 0
for value in [ x - y for x, y in zip(A, B)]:
    result_value += value ** 2
count_value = result_value / len(A)

print("Cost Function : %s" % count_value)

# 필요한 열 추출하기 ----
csv_data = housing[['lotsize','bedrooms','bathrms','stories','housing_driveway','housing_recroom','housing_fullbase','housing_gashw',
                      'housing_airco','garagepl','housing_prefarea']]
csv_label = housing['price']


# 학습 전용 데이터와 테스트 전용 데이터로 나누기 ---
train_data, test_data, train_label, test_label = \
train_test_split(csv_data, csv_label)

# 데이터 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

#정답률 구하기 ---
print("")
ac_score = metrics.accuracy_score(test_label, pre)
print("전체 데이터 수 : %d" %(len(csv_data)))
print("학습 전용 데이터 수 : %d" %(len(train_data)))
print("테스트 데이터 수 : %d" %(len(test_data)))
print("정답률 = ", ac_score)