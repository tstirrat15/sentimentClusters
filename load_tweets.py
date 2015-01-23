#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# import json
# import dataset
# import birdy
import os.path

scriptpath = os.path.dirname(os.path.abspath(__file__))

data_directory = os.path.join(scriptpath, 'data/tinySample')
data_path = os.path.join(data_directory, 'tinysample.txt')

print(os.getcwd())
print(data_path)
f = open(data_path, 'r')
content = f.read()

print("content is:")
print(content)

# The lesson: use consistent filename conventions. Christ.

# data_file = os.path.join(scriptpath, './data/tinysample/tinysample.json')
# testFile = open(data_file)
# print(testFile.read())

# files = os.listdir(data_directory)  # Get all the files in that directory
# print("Files in '%s': %s" % (data_directory, files))

# print(data_directory)

# tweets = []


# for line in open(os.path.join(data_directory, "tinysample.json"), 'r'):
#     tweets.append(line.json(object_hook=birdy.BaseTwitterClient.get_json_object_hook))

# print(tweets[1].favorite_count)
