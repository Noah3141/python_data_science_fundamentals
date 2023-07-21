# Plotting Graphs in Pandas

Pandas provides a convenient interface for basic plotting directly from DataFrames. It utilizes the Matplotlib library for generating visualizations. In this guide, we'll explore how to create different types of plots using Pandas.

## Table of Contents

1. [Line Plot](#line-plot)
2. [Bar Plot](#bar-plot)
3. [Histogram](#histogram)
4. [Scatter Plot](#scatter-plot)
5. [Pie Chart](#pie-chart)

## Line Plot

To create a line plot from a DataFrame, use the `plot()` method specifying the x and y columns. The `kind` parameter should be set to `'line'`.

```py
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
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
```

## Bar Plot

To create a bar plot from a DataFrame, use the plot() method specifying the x and y columns. The kind parameter should be set to 'bar'.

```py
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
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

```

## Histogram

To create a histogram from a DataFrame column, use the plot() method specifying the kind parameter as 'hist'.

```py
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Age': [25, 30, 35, 40, 35, 30, 45, 50, 55, 60, 65]
}

df = pd.DataFrame(data)

# Histogram
df.plot(y='Age', kind='hist', bins=5)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

```

## Scatter Plot

To create a scatter plot from a DataFrame, use the plot() method specifying the x and y columns. The kind parameter should be set to 'scatter'.

```py
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Height': [160, 165, 170, 175, 180],
    'Weight': [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Scatter plot
df.plot(x='Height', y='Weight', kind='scatter', marker='o')
plt.title('Height vs. Weight')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()

```
