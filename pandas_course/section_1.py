import pandas as pd


def demonstrate_series():
    # Creating a Series
    data = [10, 20, 30, 40, 50]
    labels = ['A', 'B', 'C', 'D', 'E']

    series = pd.Series(data, index=labels)

    print("Series:")
    print(series)


def demonstrate_dataframes():
    # Creating a DataFrame from a dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'London', 'Paris']
    }

    df = pd.DataFrame(data)

    print("\nDataFrame:")
    print(df)


def demonstrate_basic_dataframe_operations():
    # Basic DataFrame operations
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'London', 'Paris']
    }

    df = pd.DataFrame(data)

    # Selecting columns
    print("\nSelecting a single column:")
    print(df['Name'])

    # Adding a new column
    df['Country'] = ['USA', 'USA', 'UK', 'France']
    print("\nDataFrame after adding the 'Country' column:")
    print(df)

    # Selecting rows using loc (label-based indexing)
    print("\nSelecting a single row using loc:")
    print(df.loc[0])

    # Selecting rows using iloc (integer-based indexing)
    print("\nSelecting a single row using iloc:")
    print(df.iloc[1])


if __name__ == "__main__":
    print("Demonstrating Series:")
    demonstrate_series()

    print("\nDemonstrating DataFrames:")
    demonstrate_dataframes()

    print("\nDemonstrating Basic DataFrame Operations:")
    demonstrate_basic_dataframe_operations()
