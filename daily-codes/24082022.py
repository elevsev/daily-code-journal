from random import seed
from random import randrange


def train_test_split(data, split_size=0.7, seeding=seed(1)):
    seeding
    train = []
    train_size = split_size * len(data)
    data_copy = list(data)
    while len(train) < train_size:
        index = randrange(len(data_copy))
        train.append(data_copy.pop(index))
    return train, data_copy

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train, test = train_test_split(data=dataset)
print("Train:\n", train)
print("Test:\n",test)


def cross_validation(data, folds, seeding=seed(1)):
    ''' Fold size: rows / folds '''
    seeding
    data_split = []
    data_copy = list(data)
    fold_size = int(len(data) / folds)
    for i in range(folds):
        fold = []
        while len(fold) < fold_size:
            # index is the random portion that will be removed 
            index = randrange(len(data_copy))
            fold.append(data_copy.pop(index))
        data_split.append(fold)
    return data_split

number_of_folds = [3, 4, 5]
for f in number_of_folds:
    fold_ = cross_validation(data=dataset, folds=f)
    print(f"Fold size: {f}\n", fold_)

