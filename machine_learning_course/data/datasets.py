import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt  # type: ignore

# Linear correlation

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data for x-axis
num_samples = 100
x_data = np.random.rand(num_samples)

# Add some noise to x_data to make it more spread out
x_data = x_data * 10

# Generate corresponding y-data using a vague linear relationship with added noise
slope = 0.5  # Change this value to adjust the correlation strength
intercept = 2  # Change this value to adjust the correlation strength
noise_level = 1  # Change this value to adjust the noise level

y_data = slope * x_data + intercept + np.random.randn(num_samples) * noise_level

# # Plot the dataset
# plt.scatter(x_data, y_data, label="Data Points", color='b', marker='o', alpha=0.7)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("2D Dataset with Small Correlation")
# plt.legend()
# plt.grid(True)
# plt.show()

#########################################################################

# Normal distribution


# Set random seed for reproducibility
np.random.seed(42)

num_samples = 1000
mean = 100
std_dev = 22

# Generate the random data following a normal distribution
normal_dist_data = np.random.normal(mean, std_dev, num_samples)

# # Plot the normal_dist_dataset
# plt.hist(normal_dist_data, bins=30, edgecolor='black')
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Vaguely Normally Distributed Dataset")
# plt.grid(True)
# plt.show()


# Replace 'your_file_path.csv' with the actual path of your CSV file
file_path = 'C:/Users/Noah3/Coding/Python/Playground/machine_learning_course/data/train.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

print(df['SalePrice'])


plt.figure(figsize=(15, 5))
plt.scatter(df['SalePrice'], df['Fireplaces'], alpha=0.7)
# Add labels and title
plt.xlabel('SalePrice')
plt.ylabel('Fireplaces')
plt.title('Scatter Plot of House Sales Price by Number of Fireplaces')

grouped_means = df.groupby('Fireplaces')['SalePrice'].mean()
# Add vertical lines at the mean of each group
for group, mean_value in grouped_means.items():
    plt.axvline(x=mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
    plt.text(mean_value, group, f'{group}', color='red', ha='right', va='bottom', rotation=0)
plt.savefig('housing_prices_by_fireplaces.png')
# Show the plot

plt.show()
