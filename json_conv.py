import json
import os
import pprint
import time

from tqdm import tqdm


training_labels = 'C:/Users/admin/Documents/3rd Year project/OpenMV/PCB_DATASET/Train Valid Test/train/labels'
main_dict = {}
files_keys = ['filename', 'category', 'label', 'boundingBoxes']

main_dict['version'] = 1
main_dict['files'] = []

boundingBox_info_list = ['ID', 'x', 'y', 'width', 'height']

for file in os.scandir(training_labels):
    if file.is_file():

        new_intra_files_dict = dict.fromkeys(files_keys) # remember to append this to the main_dict['files'] list --> **DONE**
        new_intra_files_dict['filename'] = os.path.basename(file)
        new_intra_files_dict['category'] = "Training" # change for testing & validating
        new_intra_files_dict['label'] = {} # read each txt file and return the id -> that will be the label, e.g. mouse_bite
        new_intra_files_dict['boundingBoxes'] = [] 

        # intra-label dictionary
        new_intra_files_dict['label']['type'] = "label"
        new_intra_files_dict['label']['label'] = "defect"

        
        # Iterate through each line in each txt file, creating a dictionary for each line
        with open(file) as fh:
            for line in fh:

                boundingBox_dict = {}
                info = list(line.strip().split())
                

                for i, j in zip(boundingBox_info_list, info):
                    boundingBox_dict.update({i: j})

                    if (info[0] == '0'):
                        boundingBox_dict['ID'] = "Mouse_Bite"
                    elif (info[0] == '1'):
                        boundingBox_dict['ID'] = "Spur"
                    elif (info[0] == '2'):
                        boundingBox_dict['ID'] = "Missing_Hole"
                    elif (info[0] == '3'):
                        boundingBox_dict['ID'] = "Short_Circuit"
                    elif (info[0] == '4'):
                        boundingBox_dict['ID'] = "Open_Ciruit"
                    elif (info[0] == '5'):
                        boundingBox_dict['ID'] = "Spurious_Copper"

                    
                    time.sleep(0.005)

                new_intra_files_dict['boundingBoxes'].append(boundingBox_dict)

                pretty_data = json.dumps(new_intra_files_dict, indent = 4)
                main_dict['files'].append(pretty_data)
                
                pprint.pp(main_dict)
