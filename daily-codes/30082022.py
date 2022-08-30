print('------------------------------------------------------------------------------')
print('Class w/o set and get instances:')

class Cars:
    def __init__(self):
        self.models = {}

    def add_model(self, model_name, date):
        self.models[model_name] = date

    def get_model_date(self, model_name):
        return self.models[model_name]

bmw = Cars()
print(bmw.models)
print(bmw.add_model(model_name='X1', date='2016'))
print(bmw.add_model(model_name='X2', date='2017'))
print(bmw.add_model(model_name='X3', date='2018'))
print(bmw.get_model_date(model_name='X1'))

print('------------------------------------------------------------------------------')
print('Class w set and get instances:')
## using set + get item instances 

class Cars_get_set:
    def __init__(self):
        self.models = {}

    def __setitem__(self, key, value):
        self.models[key] = value
    
    def __getitem__(self, item):
        return self.models[item]

audi = Cars_get_set()
print(audi.models)
audi['A3'] = '2012'
audi['A4'] = '2013'
audi['A5'] = '2014'
print(audi['A3'])