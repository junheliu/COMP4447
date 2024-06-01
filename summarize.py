# This program extracts hurricane information out of a detailed North Atlantic Hurricanes information dataset
# Input file: storms-orig.csv
# Output file: new_storm_data.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('storms-orig.csv')

    dfNew = pd.DataFrame(columns=('name', 'year', 'category'))

    newDataIndex = 0

    for index, row in df.iterrows():

        if index == 0:

            currentName = row['name']
            currentCategory = 0
            currentYear = row['year']

        name = row['name']

        if pd.isnull(row['category']):
            category = 0
        else:
            category = int(row['category'])

        year = row['year']

        if name == currentName:

            if category > currentCategory:
                currentCategory = category
                currentYear = year
                continue

        else:

            if currentCategory != 0:
                dfNew.loc[newDataIndex] = [currentName, currentYear, currentCategory]
                newDataIndex = newDataIndex + 1
            currentName = name
            currentCategory = category

    print(dfNew)
    dfNew.to_csv('new_storm_data.csv')

if __name__ == "__main__":
    main()
