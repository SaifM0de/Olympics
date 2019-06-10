# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals]
# (https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table)
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals.

import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(')  # split the index by '('

df.index = names_ids.str[0]  # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)`
df = df.drop('Totals')
df


# The following function returns the first country's records in the DataFrame as a Series

def first_country():
    country = pd.Series(df.iloc[0])
    return country


first_country()


# The following function returns the country with the most gold medals in summer games as a single string value

def most_gold_summer():
    gold_summer = pd.Series(df['Gold'])
    max_gold_summer = gold_summer[gold_summer == gold_summer.max()].index[0]
    return max_gold_summer


most_gold_summer()


# The follwoing function returns the country with the biggest difference between their summer and winter gold medal counts as a single string value

def max_medal_diff():
    gold_columns = ['Gold', 'Gold.1']
    medals = df[gold_columns]
    medal_diff = pd.Series(medals['Gold'] - medals['Gold.1']).abs()
    max_diff = medal_diff[medal_diff == medal_diff.max()].index[0]
    return max_diff


max_medal_diff()


# The follwoing function returns the country with the biggest difference between their summer
# and winter gold medal counts relative to their total gold medal count as a single string value

def rel_diff_max():
    gold_1plus = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
    rel_diff = pd.Series((gold_1plus['Gold'] - gold_1plus['Gold.1']).abs()/gold_1plus['Gold.2'])
    max_diff = rel_diff[rel_diff == rel_diff.max()].index[0]
    return max_diff


rel_diff_max()


# The follwoing function returns a Series called "Points" which evaluates the weighted value of medals
# where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point

def weighted_points():
    medals_col = ['Gold.2', 'Silver.2', 'Bronze.2']
    medals = df[medals_col]
    points = pd.Series((medals['Gold.2'] * 3 + medals['Silver.2'] * 2 + medals['Bronze.2'] * 1), name='Points')
    return points


weighted_points()
