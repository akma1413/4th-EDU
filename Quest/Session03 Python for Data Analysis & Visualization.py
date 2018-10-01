# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

import numpy as np
import pandas as pd

df = pd.read_csv("C:\sex ratio.csv", engine = 'python', index_col = 0)
df.head() #1행1열에 한자가 나타나는 이유는 잘 모르겠습니다

year = []                             # 연도 리스트 만들기
for v in df.values:
    for c in df.columns.values:
        year.append(c)
print(len(year))                      #처음 만들었을때 array의 길이가 맞지않다고 하여 다시 하면서는 하나씩 길이를 확인했습니다

a = df.values                         # 성비 리스트 만들기
sr = np.array(a).tolist()
sexratio = [y for x in sr for y in x]
print(len(sexratio))

rev = pd.DataFrame.transpose(df)      # 행 인덱스를 구성하고 있던 지역 데이터를 열 인덱스로 가져와서 작업했습니다
rev.head()                            
region = []                           # 이하는 연도 리스트 만드는 과정과 동일합니다
for v in rev.values:
    for c in rev.columns.values:
        region.append(c)
print(len(region))     

temp = {"지역": region, "연도": year, "성비": sexratio} # 새로운 데이터프레임 만들기
newdf = pd.DataFrame(temp)
newdf.to_csv("C:", encoding = 'EUC-KR') # 2번은 하는대로 

# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.
