import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from typing import Sequence, Dict, Optional, Tuple


def scalizing(daf:pd.DataFrame, scale_range:Sequence[int]=(0,1), colum_list:Sequence[str]=None)->pd.DataFrame:
  for kk in colum_list:
   t = str(daf[kk].dtype)
   if "int" in t or "float" in t:
    scaler = MinMaxScaler(feature_range=scale_range)
    daf["Scaled_"+kk] = scaler.fit_transform(daf[[kk]])
  return daf   