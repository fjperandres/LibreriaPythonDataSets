import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from typing import Sequence, Dict, Optional, Tuple

def fill_na (df: pd.DataFrame, method, column_list: Sequence[str]) -> pd.DataFrame :
    
    if method == 'Drop':
        df = df[df[column_list].notna()]
    elif method == 'Mean':
        if is_numeric_dtype(df[column_list]):
           df[df[column_list].isnull()]=df[column_list].mean()
        else:
            print('No se ha podido aplicar el método porque la columna no es numérica.')
    else:
        print('Método erroneo. Solo hay las opciones Mean y Drop')

    return df