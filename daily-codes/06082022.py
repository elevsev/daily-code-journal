# linear regression - tries to fit a line of best fit to the data
# goal: minimise the error (line vs observatiions) via gradient descent
# y_pred = m * x + b

# we want to tweak m and/or b to gget the best fit ==> lowest error
# MSE = (sum(y - y_pred))**2 / n
# MSE = (sum(y - (x_i + b))**2) * 1/n

from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_df(no_rows=100):
    '''create random data in dataframe; x, y
    no_rows: number of rows required
    returns a dataframe with x,y for no_rows'''
    x = np.random.randint(0,100, size=no_rows)
    y = 0.25 * x + np.random.uniform(0, 10, x.size)  
    data = {
        'x': x,
        'y':y
        }
    df = pd.DataFrame(data=data)
    return df

df = create_df(100)

print(df.head())

# loss function ==> MSE
def mse_loss_function(m, b, observations):
    '''Returns the MSE
    MSE = (y - y_pred)**2 / n
    Steps:
    1. set total error to 0
    2. add each iteration of error to total error
    3. divide by number of observations 
    '''
    total_error = 0
    n = len(observations)
    for i in range(n):
        x = observations.iloc[i].x
        y = observations.iloc[i].y
        total_error += (y - (m * x + b)) ** 2
    total_error = total_error / n

    return total_error

# mse_example = mse_loss_function(m=0.25, b=0.5, observations=df)
# print("Total error: ", mse_example)

# calculating gradient descent
def gradient_descent(m_updated, b_updated, observations, learning_rate):
    m_gradient = 0
    b_gradient = 0
    n = len(observations)

    for i in range(n):
        x = observations.iloc[i].x
        y = observations.iloc[i].y
        m_gradient += -(2 / n) * x * (y - (m_updated * x + b_updated))
        b_gradient += -(2 / n) * (y - (m_updated * x + b_updated))
        # this gives us the direction we need to move away from to get lowest error        

        m = m_updated - m_gradient * learning_rate
        b = b_updated - b_gradient * learning_rate

        return m, b

m = 0
b = 0
L = 0.0001
epochs = 100

for epoch in range(epochs):
    if epoch % 50 == 0:
        print(f"Epoch: {epoch}")
    m, b = gradient_descent(m_updated=m, b_updated=b, observations=df, learning_rate=L)

print("m: ", m)
print("b: ", b)

def new_y(data, m_new, b_new):
    '''
    x: same
    y: updated via new m and b
    '''
    n = len(data)
    for i in range(n):
        # x_same = data.iloc[i].x
        y_new = m_new * data.iloc[i].x * b_new
    
    return y_new
    
y_new = new_y(data=df, m_new=m, b_new=b)

print(y_new)

# plt.scatter(df.x, df.y, color='blue')
# plt.plot(list(range(0, 100)), [m * x * b for x in range(0, 100)], color='green')
# plt.show()