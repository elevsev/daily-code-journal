def accuracy_score(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    accuracy = round(correct / len(actual), 2)
    return accuracy


#actual; predicted
actuals = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0]
preds = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0]

result = accuracy_score(actual=actuals, predicted=preds)
print(f"Accuracy score: {result}")