import json
import os

label_directory = 'C:/Users/admin/Documents/3rd Year project/OpenMV/PCB_DATASET/Train Valid Test/train/labels'

for file in os.scandir(label_directory):
    if file.is_file():
        print(file)