# This program cleans up North Atlantic Hurricanes information dataset
# Input file: Hurricanes-orig.csv
# Output file: new_data.csv

import pandas as pd
import re

def replaceNonAsciiWithDash(s):
    return ''.join([i if ord(i) < 128 else '-' for i in s])

def replaceNonAsciiWithSpace(s):
    return ''.join([i if ord(i) < 128 else ' ' for i in s])

def removeNonAscii(s):
    return ''.join([i if ord(i) < 128 else '' for i in s])

def insertDash(s):
    if s.find('-') != -1:
        return s
    else:
        return(re.sub(r'(\s\S*?)\s+', r'\1 - ',s))



def getYears(s):
    full_year = 0
    l = s.split(",")
    if len(l) == 1:
        short_year = int(l[0].split("-")[2])
        if short_year < 24:
            full_year = 2000 + short_year
        else:
            full_year = 1900 + short_year
    else:
        if len(l) == 3:
            full_year = l[2]
        else:
            lst = l[1].split()
            full_year = lst[0]
    return full_year

def windSpeedTransform(s):
    return removeNonAscii(s)

def pressureTransform(s):
    return replaceNonAsciiWithSpace(s)

def durationTransform(s):
    l = s.split(",")
    if len(l) == 1:
        return l[0]
    elif len(l) == 3:
        return ','.join([l[0], replaceNonAsciiWithDash(l[1]), l[2]])
    else:
        return ','.join([insertDash(replaceNonAsciiWithSpace(l[0])), removeNonAscii(l[1])])

def main():
    df = pd.read_csv('Hurricanes-orig.csv')

    print(df.head())

    print (df['Duration'])

    duration_column = df['Duration']

    new_year_column = duration_column.apply(getYears)

    df['year'] = new_year_column

    new_duration_column = duration_column.apply(durationTransform)

    df['Duration'] = new_duration_column

    wind_speed_column = df['Wind speed']

    new_wind_speed_column = wind_speed_column.apply(windSpeedTransform)

    df['Wind speed'] = new_wind_speed_column

    pressure_column = df['Pressure'].astype(str)

    new_pressure_column = pressure_column.apply(pressureTransform)

    df['Pressure'] = new_pressure_column

    df.to_csv('new_data.csv', index=False)

if __name__ == "__main__":
    main()
