# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_dict = [{'bin' : bin(key), 'dec' : key, 'hex' : hex(key), 'oct' : oct(key)} for key in range(16)]
pprint(list_dict)
