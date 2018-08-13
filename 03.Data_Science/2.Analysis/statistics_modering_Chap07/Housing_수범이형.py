import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 데이터셋을 팬더스 데이터프레임으로 읽기    ## ↱ 필드 구분 기호를 쉼표(sep=',')로 지정 // header=0 : 열 헤더를 파일 첫 행으로 지정
housing = pd.read_csv('Housing.csv', sep=',', header=0)   ## pandas의 read_csv() 함수를 사용하여 CSV 파일을 읽어 데이터프레임에 넣는다.
# housing = housing.replace('yes', '1')
# housing = housing.replace('no', '0')     ## 계산을 하기위해서 yes, no를 0과 1로 표현하였다.

## 3 상관 관계 분석
# 모든 변수 쌍 사이의 상관계수 구하기
print(housing.corr())


## 4 최소제곱법을 이용한 선형회귀분석
my_formula = 'price ~ lotsize + bedrooms + bathrms + stories + driveway + recroom + fullbase + gashw +' \
             'airco + garagepl + prefarea'


lm = ols(my_formula, data=housing).fit() ## fit이 안되면 fit_regularized()를 사용하라   ## ols는 선형함수를 표현하기 위한 하나의 방법이다.
# 또는 lm = glm(my_formula, data=housing, family=sm.families.Gaussian()).fit()

# print(lm.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))


## 6 독립변수의 표준화
# 데이터셋의 price를 종속변수로 생성
dependent_variable = housing['price']
# independet_variables = housing[housing.columns.difference(['price'])]
independet_variables = housing[housing.columns.difference(['price', 'driveway', 'recroom', 'fullbase', 'gashw', 'airco', 'prefarea'])]
independet_variables_standardized = (independet_variables - independet_variables.mean()) / independet_variables.std()
housing_standardized = pd.concat([dependent_variable, independet_variables_standardized], axis=1)
print(housing_standardized)

# lm_standardized = ols(my_formula, data=housing_standardized).fit()
# print(lm_standardized.summary())


## 7 예측하기
# 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
new_observations = housing.ix[housing.index.isin(range(10)), independet_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)