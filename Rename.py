import os

path = 'images/'

for file in os.listdir(path):
    os.rename(path + file, path + file.lower())