import pandas as pd
from typing import Sequence, Dict, Optional, Tuple, bool

def one_hot_encoding(df: pd.DataFrame,col_list: Sequence[str],keep: bool=False) -> pd.DataFrame:
  for i in range(len(col_list)):
    a = col_list[i]
    if keep == False:
      df = df.join(pd.get_dummies(df[str(a)], prefix= str(a)), how='left')
    elif keep == True:
      df = df.join(pd.get_dummies(df[str(a)], prefix= str(a)), how='left')
      del(df[str(a)])
  return df


