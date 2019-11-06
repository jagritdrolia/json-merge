import json
import sys
import os

folder_path = raw_input("Enter the folder path of your file: ")
file_prefix = raw_input("Enter the prefix of your file: ")
output_file_prefix = raw_input("Enter the prefix of your output file: ")
max_file_size = raw_input("Enter the max file size in bytes: ")

assert os.path.exists(folder_path), "I did not find the file at, "+str(user_input)
input_filenames = []

input_filenames.append(folder_path + file_prefix + '.json')

i = 1
while os.path.exists(folder_path + file_prefix + str(i) + '.json'):
    input_filenames.append(folder_path + file_prefix + str(i) + '.json')
    i = i+1

all_data = {}
for file in input_filenames:
    with open(file, "r") as f:
        data = json.load(f)
    for key in data:
        if key in all_data:
            all_data[key] += data[key]
        else:
            all_data[key] = data[key]
with open(output_file_prefix + '.json', "w") as outfile:
    json.dump(all_data, outfile)

statinfo = os.stat('result.json')
print(statinfo.st_size)
