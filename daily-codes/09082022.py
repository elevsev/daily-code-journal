import numpy as np

outcomes = np.random.randint(0,2,size=100)

def probability_of_bad(data):
    data = data.tolist()
    n = len(data)
    bad = data.count(1)
    pr_bad = bad / n
    return pr_bad

result = probability_of_bad(data=outcomes)
print(f"Probability of bads: {result}")