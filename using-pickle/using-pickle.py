import pickle
import bz2

dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5,
             'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}


filename = 'dogs'
with open(filename, 'wb') as outfile:
    pickle.dump(dogs_dict, outfile)


with open(filename, 'rb') as infile:
    dict_result = pickle.load(infile)
    print(dict_result)
    print(type(dict_result))


sfile = bz2.BZ2File('smallerdogs', 'w')
pickle.dump(dogs_dict, sfile)
