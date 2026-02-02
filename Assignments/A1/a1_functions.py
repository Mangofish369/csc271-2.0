"""CSC108: Winter 2026 -- Assignment 1: Canadian Border Crossings

This code is provided solely for the personal and private use of students
taking the CSC271H1 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2026 CSC271H1 Teaching Team
"""

import pandas as pd
import numpy as np

# Column labels
DATE = 'Date'
REGION = 'Region'
MODE = 'Mode'
VOLUME = 'Volume'
PORT_ID = 'Port ID'
PORT_NAME = 'Port Name'

# Fill strategies
MEAN = 'mean'
MEDIAN = 'median'
ZERO = 'zero'

### Provided Helper Function ###

def load_data(file_path: str) -> pd.DataFrame:
    """Return the data from the CSV file named file_path as a DataFrame."""

    return pd.read_csv(file_path)

### Task 1: Data Cleaning and Preparation ###
def clean_volume(df: pd.DataFrame) -> None:
    df["Sum of Volume"] = df["Sum of Volume"].astype("int64")
    df.rename(columns = {"Sum of Volume": VOLUME}, inplace=True)

def clean_region(df: pd.DataFrame) -> None:
    df[REGION] = df[REGION].str.removesuffix(" Region")
    df[REGION] = df[REGION].str.title()

def clean_port(df: pd.DataFrame) -> None:
    port_list = df["Port of Entry"].str.split(expand = True)
    df[PORT_ID] = port_list.iloc[:,0]
    df[PORT_NAME] = port_list.iloc[:, 2]
    df.drop(columns = ["Port of Entry"], inplace = True)

def clean_data(df: pd.DataFrame) -> None:
    pd.to_datetime(df[DATE])
    clean_region(df)
    clean_volume(df)
    clean_port(df)

def fill_missing_volumes(df: pd.DataFrame, method: str) -> None:
    if method == MEAN:
        mean = df['Sum of Volume'].mean()
        df['Sum of Volume'] = df['Sum of Volume'].fillna(mean)
    elif method == MEDIAN:
        median = df['Sum of Volume'].median()
        df['Sum of Volume'] = df['Sum of Volume'].fillna(median)


### Task 2: Data Exploration and Analysis Functions ###
def filter_with_volume(df: pd.DataFrame, column: str, value: str, volume: int) -> pd.DataFrame:
    filter = df[(df[column] == value) & (df[VOLUME] >= volume)]
    return filter



if __name__ == "__main__":
    path = r"Assignments\A1\traveller-report-daily.csv"
    border_df = load_data(path)
    fill_missing_volumes(border_df,'median')
    clean_data(border_df)

    abc = filter_with_volume(border_df,REGION,'Atlantic',1000)
    print(border_df.head())
    print(abc)

    # # You may call on your functions here to test them.

    # border_df = load_data('Assignments\A1\traveller-report-daily.csv')
    # #clean_data(border_df)
    # #fill_missing_volumes(border_df)