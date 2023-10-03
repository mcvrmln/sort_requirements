"""
A simple script to sort a tree-like structure

"""

import pandas as pd


def read_data(file: str) -> pd.DataFrame:
    """
    Read the data

    """
    dtypes = {'ID': str, 'Parent-ID' : str}

    # data = {'id': ['AA', 'AB', 'AC', 'BC', 'BD', 'CA', 'CB', 'CD'], 
    #         'parent_id': [None, 'AA', 'AA', 'AB', 'AB', 'AC', 'CA', 'CB'], 
    #         'description': [ None, 'First requirement', 'Second requirement',
    #                          'Something else', 'An item','An other item', 'What is this',  'Last Node'] }
    df = pd.read_excel(file, header=1, dtype=dtypes)
    return df


def find_children(df: pd.DataFrame, parent: str, grandparents:str) -> pd.DataFrame:
    """
    
    """
 
    if len(grandparents) > 0:
        sep = '_'
    else:
        sep = ''

    grandparents = f'{grandparents}{sep}{parent}'
    sep = '_' 
    mask = df['Parent-ID']==parent
    df.loc[mask, 'long_id'] = df.apply(lambda row : f"{grandparents}{sep}{str(row['ID'])}", axis = 1)
 
    if len(df.loc[mask,]) > 0:
        for index, row in df.loc[mask,].iterrows():
            find_children(df, row.ID, grandparents)
    
    return df



def run_app():
    """
    Main function of this script
    """
    file = r'../data/requirements.xlsx'
    df = read_data(file)
    if len(df) == df.ID.nunique():
        print('Only unique keys!')
        mask = df['ID'].str.fullmatch('1')
        df.loc[mask, 'long_id'] = 'Base'
        find_children(df, '1', '')
        print(df.head(10))
    else: 
        print('Dataset contains a not unique key (id)!')
    df.to_excel(file, sheet_name='Sorted', index=False)

if __name__ == "__main__":
    run_app()
