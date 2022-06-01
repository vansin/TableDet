import json
import pickle

data = []

for i in range(1000000):
    data.append(i)

with open('/project/train/models/1.pb', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f)


with open('/project/train/log/log.txt', 'w') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    # pickle.dump(data, f)
    f.write('fdsafdsaf')


print('ensure output python file run well')
