from cmath import log
from turtle import color
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets 
import matplotlib.pyplot as plt
import math

class LogisticRegression:
    def __init__(self, L=0.001, iterations=1000):
        self.L = L
        self.iterations = iterations
        self.weights = None
        self.bias = None 

    def fit(self, X, y):
        '''
        INPUTS ->
         - X: 2D vector; m (rows) x n (features)
         - y: 1D array; m (rows)
        '''
        # init samples
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # gradient descent; iteratively update the weights
        for iteration in range(self.iterations):
            # linear model
            linear_model = np.dot(X, self.weights) + self.bias 
            # approximation of y
            y_prediction = self._sigmoid(linear_model)
            # update w, and b via derivatives
            dw = (2 / n_samples) * np.dot(X.T, (y_prediction - y))
            db = (2 / n_samples) * np.sum((y_prediction - y))

            # update the weights 
            self.weights -= self.L * dw
            self.bias -= self.L * db

    def predict(self, X):
        # linear model
        linear_model = np.dot(X, self.weights) + self.bias 
        # approximation of y
        y_prediction = self._sigmoid(linear_model) 
        y_pred_classes = [1 if i > 0.5 else 0 for i in y_prediction]
        return y_pred_classes

    def _sigmoid(self, x):
        sig = 1 / (1 + np.exp(-x))
        return sig


data = datasets.load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=69)

def accuracy(y_actual, y_predicted):
    accuracy = np.sum(y_actual == y_predicted) / len(y_actual)
    return accuracy

logreg = LogisticRegression()
print(logreg.bias)
print(logreg.weights)
print(logreg.iterations)
print(logreg.L)

lr_fit = logreg.fit(X=X_train, y=y_train)
print(lr_fit)
preds = logreg.predict(X=X_test)
print(preds)
acc = accuracy(y_actual=y_test, y_predicted=preds)
print(f"Accuracy: {acc}")


plt.barh(y_test, width=10, color='blue')
plt.show()
plt.barh(preds, width=10, color='red')
plt.show()