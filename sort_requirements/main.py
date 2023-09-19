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
    df_children = df[df['parent_id']==parent]
    

    if len(grandparents) > 0:
        sep = '_'
    else:
        sep = ''

    grandparents = f'{grandparents}{sep}{parent}'
    df_children = df_children.assign(long_id=lambda x: (f"{grandparents}{sep}{str(x['id'])}"))

    if len(df_children) > 0:
        for index, row in df_children.iterrows():
            print(f"{grandparents} has child {row['id']}: {row['description']}")
            pd.concat([df_children, find_children(df, row.id, grandparents)], ignore_index=True)
    
    return df_children



def run_app():
    """
    Main function of this script
    """
    df = read_data()
    if len(df) == df.id.nunique():
        print('Only unique keys!')
        sorted_df = df[df['id']=='AA']
        sorted_df['long_id'] = None
        temp_df = find_children(df, 'AA', '')
        pd.concat([sorted_df, temp_df], ignore_index=True)
        print(temp_df.head(10))
    else: 
        print('Dataset contains a not unique key (id)!')


if __name__ == "__main__":
    run_app()
