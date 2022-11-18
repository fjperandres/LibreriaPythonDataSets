import pandas as pd
from typing import Sequence, Dict, Optional, Tuple


def scalizing(daf:pd.DataFrame, scale_range:Sequence[int]=[0,1], colum_list:Sequence[str]=None):
  for kk in colum_list:
    t = str(daf[kk].dtype)
    if "int" in t or "float" in t:
      scaler = MinMaxScaler(feature_range=scale_range)
      daf[["Scaled"+colum_list[kk]]] = scaler.fit_transform(colum_list[kk])
  return daf       