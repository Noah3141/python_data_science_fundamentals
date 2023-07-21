import pandas as pd
import matplotlib.pyplot as plt


def demonstrate_basic_plotting():
    # Basic Plotting
    data = {
        'Year': [2010, 2011, 2012, 2013, 2014],
        'Sales': [100, 150, 200, 180, 250],
        'Expenses': [80, 100, 120, 110, 150]
    }

    df = pd.DataFrame(data)

    # Line plot
    df.plot(x='Year', y=['Sales', 'Expenses'], kind='line', marker='o', linestyle='--')
    plt.title('Sales and Expenses Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.show()


def demonstrate_customizing_plots():
    # Customizing Plots
    data = {
        'Month': ['January', 'February', 'March', 'April', 'May'],
        'Temperature': [20, 22, 25, 28, 30],
        'Precipitation': [10, 15, 5, 8, 12]
    }

    df = pd.DataFrame(data)

    # Bar plot
    ax = df.plot(x='Month', y=['Temperature', 'Precipitation'], kind='bar', color=['blue', 'green'])
    plt.title('Temperature and Precipitation by Month')
    plt.xlabel('Month')
    plt.ylabel('Value')
    plt.legend(title='Category', labels=['Temperature', 'Precipitation'])

    # Remove x-axis label rotation
    plt.xticks(rotation=0)

    # Add values above each bar
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center')

    plt.show()


if __name__ == "__main__":
    print("Demonstrating Basic Plotting:")
    demonstrate_basic_plotting()

    print("\nDemonstrating Customizing Plots:")
    demonstrate_customizing_plots()
