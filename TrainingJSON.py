import json
import os
import pprint
import time

from tqdm import tqdm


training_labels = 'C:/Users/admin/Documents/3rd Year project/OpenMV/PCB_DATASET/Train Valid Test/train/labels'
main_dict = {}
files_keys = ['path', 'category', 'label', 'boundingBoxes']

main_dict['version'] = 1
main_dict['files'] = []

boundingBox_info_list = ['label', 'x', 'y', 'width', 'height']

for file in os.scandir(training_labels):
    if file.is_file():

        new_intra_files_dict = dict.fromkeys(files_keys) # remember to append this to the main_dict['files'] list --> **DONE**

        root = os.path.splitext(file.name)[0]
       

        new_intra_files_dict['path'] = "l_" + f"{root}" + ".jpg"     
        
        new_intra_files_dict['category'] = "Training" # change for testing & validating
        new_intra_files_dict['label'] = {} # read each txt file and return the id -> that will be the label, e.g. mouse_bite
        new_intra_files_dict['boundingBoxes'] = [] 

        # intra-label dictionary
        new_intra_files_dict['label']['type'] = "label"
        new_intra_files_dict['label']['label'] = "defect"

        
        # Iterate through each line in each txt file, creating a dictionary for each line
        with open(file) as fh:
            for line in fh:

                
                id, x, y, w, h = line.strip().split()
                boundingBox_dict = {
                    "label" : None,
                    "x" : float(x),
                    "y" : float(y),
                    "width" : float(w),
                    "height" : float(h)
                    }
                
                id_map = {
                    "0": "mouse_bite",
                    "1": "Spur",
                    "2": "missing_hole",
                    "3": "short_circuit",
                    "4": "open_circuit",
                    "5": "spurious_copper"
                }

                boundingBox_dict["label"] = id_map.get(id, "Unknown") #return "Unknown" if id not found
                time.sleep(0.005)

                new_intra_files_dict['boundingBoxes'].append(boundingBox_dict)
                main_dict['files'].append(new_intra_files_dict)

with open("train_labels.json", "w") as out_train:
    json.dump(main_dict, out_train, indent = 4)





