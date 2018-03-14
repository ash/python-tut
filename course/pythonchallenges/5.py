import pickle
import urllib.request

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
decoded_data = pickle.load(f)
#print(decoded_data)

for r in decoded_data:
    for c in r:
        (char, repetitions) = c
        print(char * repetitions, end='')
    print('')