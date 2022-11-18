# Funcion (DF, method,columns) -> return DF
import pandas as pd
import numpy as np
from typing import Sequence, Dict, Optional, Tuple


def fill_na (df: pd.DataFrame, method, column_list: Sequence[str]) -> pd.DataFrame :
    
    if method == 'Drop':
        df = df[df[column_list].notna()]
    elif method == 'Mean':
        if df.dtypes(column_list).contains('int') or df.dtypes(column_list).contains('float'):
            df = df.loc[df[column_list].isnull(), column_list]= df[column_list].mean()
        else:
            print('No se ha podido aplicar el método porque la columna no es numérica.')
    else:
        print('Método erroneo. Solo hay las opciones Mean y Drop')

    return df