import pandas as pd


def demonstrate_exploratory_data_analysis():
    # Exploratory Data Analysis (EDA)
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'London', 'Paris']
    }

    df = pd.DataFrame(data)

    # Descriptive statistics
    print("Descriptive Statistics:")
    print(df.describe())

    # Value counts for a categorical column
    print("\nValue Counts for 'City' column:")
    print(df['City'].value_counts())


def demonstrate_groupby_aggregation():
    # Aggregation using groupby
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Age': [25, 30, 35, 40, 35, 30],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'London', 'Paris'],
        'Salary': [50000, 60000, 55000, 70000, 60000, 75000]
    }

    df = pd.DataFrame(data)

    # Grouping by a column and calculating mean salary for each city
    grouped_df = df.groupby('City')['Salary'].mean()

    print("\nOriginal DataFrame:")
    print(df)
    print("\nGrouped DataFrame - Mean Salary for each City:")
    print(grouped_df)


if __name__ == "__main__":
    print("Demonstrating Exploratory Data Analysis:")
    demonstrate_exploratory_data_analysis()

    print("\nDemonstrating Groupby and Aggregation:")
    demonstrate_groupby_aggregation()
