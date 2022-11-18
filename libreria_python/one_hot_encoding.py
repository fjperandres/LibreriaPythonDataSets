import pandas as pd
from typing import Sequence, Dict, Optional, Tuple, bool

def one_hot_encoding(df: pd.DataFrame,col_list: Sequence[str],keep: bool=False) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): DataFrame
        col_list (Sequence[str]): List of columns to process.
        keep (bool, optional): Variable to ignore the column on DataFrame. True: Keeps original columns, False: Ignore original columns. Defaults to False.

    Returns:
        pd.DataFrame: _description_
    """    
    for i in range(len(col_list)):
        a = col_list[i]
        if keep == False:
            df = df.join(pd.get_dummies(df[str(a)], prefix= str(a)), how='left')
            del(df[str(a)])
        elif keep == True:
            df = df.join(pd.get_dummies(df[str(a)], prefix= str(a)), how='left')
        
    return df