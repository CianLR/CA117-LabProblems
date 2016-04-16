import sys
from math import pi

precision = sys.argv[1]
formatstring = '%.' + precision + 'f'
print(formatstring%pi)
