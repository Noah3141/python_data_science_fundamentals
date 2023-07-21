import pandas as pd
from pandas import DataFrame


def demonstrate_data_cleaning():
    # Data Cleaning: Handling missing values and duplicates
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', None, 'David', 'Alice'],
        'Age': [25, 30, None, 40, 35, 25],
        'City': ['New York', 'San Francisco', 'London', 'Paris', None, 'New York']
    }

    df = pd.DataFrame(data)

    # Checking for missing values
    print("DataFrame with missing values:")
    print(df)

    print("\nChecking for missing values in each column:")
    print(df.isnull().sum())

    # Handling missing values: drop rows with missing values
    df_cleaned = df.dropna()

    print("\nDataFrame after dropping rows with missing values:")
    print(df_cleaned)

    # Handling duplicates: drop duplicate rows
    df_deduplicated = df_cleaned.drop_duplicates()

    print("\nDataFrame after removing duplicate rows:")
    print(df_deduplicated)


def demonstrate_data_manipulation():
    # Data Manipulation: Filtering and applying functions
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'London', 'Paris']
    }

    df = DataFrame(data)

    # Filtering rows based on a condition
    filtered_df = df[df['Age'] > 30]

    print("\nOriginal DataFrame:")
    print(df)
    print("\nFiltered DataFrame (age > 30):")
    print(filtered_df)

    # Applying a function to a column
    def add_years(age):
        return age + 5

    df['Age'] = df['Age'].apply(add_years)

    print("\nDataFrame after applying 'add_years' function to 'Age' column:")
    print(df)


if __name__ == "__main__":
    print("Demonstrating Data Cleaning:")
    demonstrate_data_cleaning()

    print("\nDemonstrating Data Manipulation:")
    demonstrate_data_manipulation()
