import os
import sys

for filename in os.listdir("."):
   s = ''
   try:
      s = open(filename, encoding='UTF-8').read()
   except:
      s = open(filename).read()
   print(s.count('"http'))
