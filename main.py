
import pandas as pd
from src import cleaning, functions


if __name__ == '__main__':
    try:
        shark_attacks = pd.read_csv("data/attacks.csv", encoding="latin1")
        shark_attacks = cleaning.clean_dataframe(shark_attacks)
        functions.export_to_csv(shark_attacks, 'data/clean_attacks')
    except Exception as e:
        print('You need to add the original dataset into data folder :)')
