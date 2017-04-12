# Question - 1:  Create a dataframe with with following data cleanup to make this file redable.
# - Skip first row
# - Rename column containing 01, 02 and 03 to Gold, Silver and Bronze
# - Split country name and country code and add country name as data frame index
# - Drop column Totals

# Question-2 : What is the first country in dataframe? Write a function to return first country detail.

# Question – 3: Which country has won the most gold medals in summer games?

# Question - 4: Which country had the biggest difference between their summer and winter gold medal counts?

# Question - 5: Write a function to update the dataframe to include a new column called "Points" for Games which
# is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze
# mdeals for 1 point. The function should return only the column (a Series object) which you created.


import pandas as pd


def cleanup_csv():
    df = pd.read_csv('data/olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
        if col[:2] == '02':
            df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
        if col[:2] == '03':
            df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)

    names_ids = df.index.str.split('(')  # split the index by '('
    df.index = names_ids.str[0]  # the [0] element is the country name (new index)
    df = df.drop('Totals')
    df.head()
    return df


def first_country(df):
    series = df.iloc[0]
    return series


def gold_medal(df):
    x = max(df['Gold'] - df['Gold.1'])
    ans = df[(df['Gold'] - df['Gold.1']) == x].index.tolist()
    return ans[0]


def biggest_different_in_gold_medal(df):
    x = max(df['Gold'] - df['Gold.1'])
    ans = df[(df['Gold'] - df['Gold.1']) == x].index.tolist()
    return ans[0]


def get_points(df):
    Points = 3 * df['Gold.2'] + 2 * df['Silver.2'] + 1 * df['Bronze.2']
    return Points


# dataframe = cleanup_csv()
# series = get_points(dataframe)
# print(type(series))
# print(series)