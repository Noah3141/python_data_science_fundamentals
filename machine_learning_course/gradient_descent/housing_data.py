import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def compute_cost(x, y, w, b):
    # Function to calculate the cost
    m = x.shape[0]
    cost = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost = cost + (f_wb - y[i])**2
    total_cost = 1 / (2 * m) * cost

    return total_cost


def compute_gradient(x, y, w, b):
    """
    Computes the gradient for linear regression 
    Args:
      x (ndarray (m,)): Data, m examples 
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters  
    Returns
      dj_dw (scalar): The gradient of the cost w.r.t. the parameter w
      dj_db (scalar): The gradient of the cost w.r.t. the parameter b     
     """

    # Number of training examples
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w * x[i] + b  # My equations prediction for the y value
        dj_dw_i = (f_wb - y[i]) * x[i]  # The difference between my equation's SLOPE prediction, and the actual
        dj_db_i = f_wb - y[i]  # The difference between my equation's y POSITION prediction, and the actual
        dj_db += dj_db_i
        dj_dw += dj_dw_i
    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db


def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function) -> tuple[any, any, list, list]:
    """
    Performs gradient descent to fit w,b. Updates w,b by taking 
    num_iters gradient steps with learning rate alpha

    Args:
      x (ndarray (m,))  : Data, m examples 
      y (ndarray (m,))  : target values
      w_in,b_in (scalar): initial values of model parameters  
      alpha (float):     Learning rate
      num_iters (int):   number of iterations to run gradient descent
      cost_function:     function to call to produce cost
      gradient_function: function to call to produce gradient

    Returns:
      w (scalar): Updated value of parameter after running gradient descent
      b (scalar): Updated value of parameter after running gradient descent
      J_history (List): History of cost values
      p_history (list): History of parameters [w,b] 
      """

    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    p_history = []
    b = b_in
    w = w_in

    for i in range(num_iters):
        # Calculate the gradient and update the parameters using gradient_function
        dj_dw, dj_db = gradient_function(x, y, w, b)

        # Update Parameters using equation (3) above
        b = b - alpha * dj_db
        w = w - alpha * dj_dw

        # Save cost J at each iteration
        if i < 100_000:      # prevent resource exhaustion
            J_history.append(cost_function(x, y, w, b))
            p_history.append([w, b])
        # Print cost every at intervals 10 times or as many iterations if < 10
        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e}  ",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")

    return w, b, J_history, p_history  # return w and J,w history for graphing


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Replace 'your_file_path.csv' with the actual path of your CSV file
file_path = 'C:/Users/Noah3/Coding/Python/Playground/machine_learning_course/data/train.csv'

data = pd.read_csv(file_path)
years_built = np.array(data["YearBuilt"])  # x - feature
prices = np.array(data["SalePrice"])  # y - target value

data.plot.scatter(x='YearBuilt', y='SalePrice', c='r', alpha=0.7)
plt.title('Sales Price By Year Built')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.grid(True)
plt.show()
# # truncate datasets for memory
# prices = prices[0:5]
# years_built = years_built[0:5]


# initialize parameters
w_init = .7
b_init = 50_000
# some gradient descent settings
iterations = 5_000
tmp_alpha = 8.0e-8
# run gradient descent
w_final, b_final, J_hist, p_hist = gradient_descent(years_built, prices, w_init, b_init, tmp_alpha,
                                                    iterations, compute_cost, compute_gradient)
print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(12, 4))
ax1.plot(J_hist[:100])
ax2.plot(1000 + np.arange(len(J_hist[1000:])), J_hist[1000:])
ax1.set_title("Cost vs. iteration (start)")
ax2.set_title("Cost vs. iteration (end)")
ax1.set_ylabel('Cost')
ax2.set_ylabel('Cost')
ax1.set_xlabel('iteration step')
ax2.set_xlabel('iteration step')
plt.show()

print(f"1998 house prediction ${w_final*1998 + b_final:.2f}")
print(f"1920 house prediction ${w_final*1920 + b_final:.2f}")
print(f"2021 sqft house prediction ${w_final*2021 + b_final:.2f}")

data.plot.scatter(x='YearBuilt', y='SalePrice', c='r', alpha=0.7)
plt.title('Sales Price By Year Built')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.grid(True)

x_range = range(data['YearBuilt'].min(), data['YearBuilt'].max())
y_values = np.array([w_final * x + b_final for x in x_range])
plt.plot(x_range, y_values, color='black', label=f'y = {w_final}x + {b_final}')


plt.show()

x = 5; print(x);
y = 3; print(y)
