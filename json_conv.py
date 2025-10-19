import json
import os

training_labels = 'C:/Users/admin/Documents/3rd Year project/OpenMV/PCB_DATASET/Train Valid Test/train/labels'

main_dict = {}

#main_fields = ['version', 'files']
files_keys = ['filename', 'category', 'label', 'boundingBoxes']



main_dict['version'] = 1
main_dict['files'] = []

boundingBox_info_list = ['label', 'x', 'y', 'width', 'height']
boundingBox_info_dict = dict.fromkeys(boundingBox_info_list)

for file in os.scandir(training_labels):
    if file.is_file():
        new_intra_files_dict = dict.fromkeys(files_keys) # remember to append this to the main_dict['files'] list

        # main dictionary for each image file 
        new_intra_files_dict['filename'] = os.path.basename(file)
        new_intra_files_dict['Label'] = {} # read each txt file and return the id -> that will be the label, e.g. mouse_bite
        new_intra_files_dict['boundingBoxes'] = [] #read each file and return coordinates and its width and height
        new_intra_files_dict['category'] = "Training" # change for testing & validating

        # intra-label dictionary
        new_intra_files_dict['Label']['type'] = "label"
        new_intra_files_dict['Label']['label'] = "defect"

        pretty_data = json.dumps(new_intra_files_dict, indent = 4)
        main_dict['files'].append(pretty_data)

       # print(main_dict)

        i = 0
        with open(file) as fh:
            for line in fh:
                new_intra_files_dict['boundingBoxes'].append(boundingBox_info_dict)
                info = list(line.strip().split())
                while i<len(boundingBox_info_list):
                    boundingBox_info_dict[i] = info[i]
                    i = i + 1
                  
            
        print(boundingBox_info_dict)