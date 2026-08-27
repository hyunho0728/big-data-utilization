import numpy as np
import pandas as pd

info = pd.read_csv("waist.csv")

# 데이터가 누락된 행은 삭제하는 코드를 작성하세요.
info.dropna(inplace=True)

# 지시사항을 참고하여 허리둘레를 inch 단위로 변환하는 식을 적용하는 코드를 작성하세요
info["허리둘레(inch)"] = info["허리둘레"] / 2.54

info["허리둘레(inch)"] = info["허리둘레(inch)"].astype(int)

info_column_add = info
print(info_column_add)