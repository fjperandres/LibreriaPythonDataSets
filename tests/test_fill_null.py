# Funcion (DF, method,columns) -> return DF
import pandas as pd
import numpy as np
from typing import Sequence, Dict, Optional, Tuple


def fill_na (df: pd.DataFrame, method, column_list: Sequence[str]) -> pd.DataFrame :
    
    if method == 'Drop':
        df = df[df['Column'].notna()]
    elif method == 'Mean':
        df = df[df['Column'].notna()]
    else:
        print('Método erroneo. Solo hay las opciones Mean o Drop')

    return df