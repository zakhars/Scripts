import os

for filename in os.listdir("."):
    if filename.endswith('.jpg'):
        os.rename(filename, filename.zfill(4 + len('.jpg')))
