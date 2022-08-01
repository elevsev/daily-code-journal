class Means:
    def __init__(self, x_values, weights):
        self.x_values = x_values
        self.weights = weights
        self.n = len(self.x_values)

    def simple_mean(self):
        '''xm = sum(x)/n'''
        self.x_m = sum(self.x_values) / self.n
        return self.x_m

    def weighted_mean(self):
        '''xw = (sum(w * x)) / (sum(w))'''
        numerator = sum(w * x for w,x in zip(self.x_values, self.weights))
        denomenator = sum(self.weights)
        self.x_w = numerator / denomenator
        return self.x_w


x_values = [2, 4, 6]
weights = [0.2, 0.5, 0.3]

result = Means(x_values=x_values, weights=weights)

print(result.simple_mean())
print(result.weighted_mean())