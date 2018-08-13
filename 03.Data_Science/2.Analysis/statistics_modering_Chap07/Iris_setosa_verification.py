import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

iris = pd.read_csv('iris.csv',sep=',', header=0)
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace(".","_")]

iris['iris01'] = np.where(iris['variety'] == 'Setosa',1.,0.)

dependent_variable = iris['iris01']
independent_variables = iris[['sepal_length','sepal_width','petal_length','petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

sample_data_index_list = [2,30,40,50,71,86,100,104,120,145]
# 값의 크기가 정렬이 되지 않아도 index순서로 정렬된다.
new_observations = iris.ix[iris.index.isin(sample_data_index_list), independent_variables.columns]
# new_observations = iris.ix[iris.index.isin(random.sample(range(150),10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)

print("\n샘플링 데이터 예측 테스트")
print("10개 샘플링 데이터 리스트")
print(new_observations_with_constant.head(10))
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]

index = 1
for pridicted_value in y_predicted_rounded:
    if pridicted_value == 1.0:
        print("%d번째 샘플링 데이터 예측 결과: Setosa 확실"%index)
    else:
        print("%d번째 샘플링 데이터 예측 결과: Setosa 아닌 다른 품종"%index)
    index+=1

