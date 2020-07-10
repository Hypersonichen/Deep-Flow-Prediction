#import json
import pickle

with open('max_inputs.pickle', 'rb') as f: a,b,c = pickle.load(f)
f.close()
print(a,b,c)
with open('max_targets.pickle', 'rb') as f: a,b,c = pickle.load(f)
f.close()
print(a,b,c)
