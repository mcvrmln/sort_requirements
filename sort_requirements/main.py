"""
A simple script to sort a tree-like structure

"""

import pandas as pd


def read_data() -> pd.DataFrame:
    """
    Read the data

    """

    data = {'id': ['AA', 'AB', 'AC', 'BC', 'BD', 'CA', 'CB', 'CD'], 
            'parent_id': [None, 'AA', 'AA', 'AB', 'AB', 'AC', 'CA', 'CB'], 
            'description': [ None, 'First requirement', 'Second requirement',
                             'Something else', 'An item','An other item', 'What is this',  'Last Node'] }
    return pd.DataFrame(data)


def find_children(df: pd.DataFrame, parent: str, grandparents:str) -> pd.DataFrame:
    """
    
    """
 
    if len(grandparents) > 0:
        sep = '_'
    else:
        sep = ''

    grandparents = f'{grandparents}{sep}{parent}'
    sep = '_' 
    mask = df['parent_id']==parent
    df.loc[mask, 'long_id'] = df.apply(lambda row : f"{grandparents}{sep}{str(row['id'])}", axis = 1)
 
    if len(df.loc[mask,]) > 0:
        for index, row in df.loc[mask,].iterrows():
            find_children(df, row.id, grandparents)
    
    return df



def run_app():
    """
    Main function of this script
    """
    df = read_data()
    if len(df) == df.id.nunique():
        print('Only unique keys!')
        mask = df['id'].str.fullmatch('AA')
        df.loc[mask, 'long_id'] = 'Base'
        find_children(df, 'AA', '')
        print(df.head(10))
    else: 
        print('Dataset contains a not unique key (id)!')


if __name__ == "__main__":
    run_app()
