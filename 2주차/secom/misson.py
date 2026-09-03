# 이 셀은 그대로 실행하세요.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pathlib import Path

_have = {f.name for f in fm.fontManager.ttflist}
for _f in ['Malgun Gothic', 'AppleGothic', 'NanumGothic', 'DejaVu Sans']:
    if _f in _have:
        plt.rcParams['font.family'] = _f
        break
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', 30)

DATA = Path('./secom')   # 폴더를 옮겼다면 이 줄만 고치세요

def check(name, cond, hint=''):
    if cond:
        print('[통과] ' + name)
    else:
        print('[실패] ' + name + (('  ->  ' + str(hint)) if hint else ''))

print('폰트:', plt.rcParams['font.family'][0], '| 데이터 폴더:', DATA.exists())

# TODO 1-1: 두 파일 불러오기
#   힌트: pd.read_csv(DATA / '파일명', encoding='utf-8-sig', parse_dates=['timestamp'])
df = pd.read_csv(DATA / 'secom_equipment.csv', encoding='utf-8-sig', parse_dates=['timestamp'])
meta = pd.read_csv(DATA / 'signal_metadata.csv', encoding='utf-8-sig')

# TODO 1-2: 두 데이터의 크기 출력
print(f'df size : {len(df)}, meta size : {len(meta)}')

# TODO 1-3: 불량 건수와 비율(%)
n_fail = len(df[df['label'] == 1])
fail_rate = n_fail / len(df) * 100

check('데이터 로드', df is not None and meta is not None, '두 파일을 읽어오세요')
check('df 크기 1567 x 594', df is not None and df.shape == (1567, 594), None if df is None else df.shape)
check('meta 590행', meta is not None and len(meta) == 590)
check('불량 104건', n_fail == 104, n_fail)
check('불량률 6.64%', fail_rate is not None and abs(fail_rate - 6.64) < 0.05, fail_rate)

# TODO 2-1: SIG_ 로 시작하는 컬럼 이름만 모으기
sig_cols = None

# TODO 2-2: 신호별 결측 비율 (힌트: .isna().mean())
miss = None

# TODO 2-3: 결측이 많은 상위 10개 출력


# TODO 2-4: 결측 50%를 넘는 신호 이름 리스트
high_missing = None