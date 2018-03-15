import pickle

data = [1,2,3,{'a':'b'}]

with open('data.pck', 'wb') as f:
    pickle.dump(data, f)

with open('data.pck', 'rb') as f:
    data = pickle.load(f)
    print(data)
