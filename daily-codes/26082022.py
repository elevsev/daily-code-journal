def zero_rule_algo(x, y):
    output = [row[-1] for row in x]
    predicted = max(set(output), key=output.count)
    updated = [predicted for i in range(len(y))]
    print('Output', output)
    print('Predicted', predicted)
    print('Updated', updated)

x_ = [[0],[0],[0],[0],[1],[1],[1],[0],[1],[0]]
y_ = [[None], [None], [None]]
algo = zero_rule_algo(x=x_, y=y_)
print(algo)