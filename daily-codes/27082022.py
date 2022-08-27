# def covariance(x, mean_x, y, mean_y):
#     covariance = 0.0
#     for i in range(len(x)): 
#         covariance += ((x[i] - mean_x) * (y[i] - mean_y))
#     return covariance


class Metrics:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def mean(self):
        self.mean_x = sum(self.x) / len(self.x)
        self.mean_y = sum(self.y) / len(self.y)
        return self.mean_x, self.mean_y

    def covariance(self):
        self.covariance = 0.0
        for i in range(len(self.x)): 
            self.covariance += ((self.x[i] - self.mean_x) * (self.y[i] - self.mean_y))
        return self.covariance


x_ = [1,2,3,4,5]
# 15/5 = 3
y_ = [2,4,6,8,10]
# 30/5 = 6

result = Metrics(x=x_, y=y_)
mean_x, mean_y = result.mean()
print(f"Mean X: {mean_x}")
print(f"Mean Y: {mean_y}")

covar = result.covariance()
print(f"Covariance between X and Y: {covar}")