import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from typing import Sequence, Dict, Optional, Tuple


def scalizing(daf:pd.DataFrame, colum_list: Sequence[str], scale_range:Sequence[int]=(0,1))->pd.DataFrame:
  for kk in colum_list:
   t = str(daf[kk].dtype)
   if "int" in t or "float" in t:
    scaler = MinMaxScaler(feature_range=scale_range)
    daf["Scaled_"+kk] = scaler.fit_transform(daf[[kk]])
  return daf   