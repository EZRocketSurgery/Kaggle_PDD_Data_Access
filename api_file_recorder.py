from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime
import common_methods
api = KaggleApi()
api.authenticate()

#read the target dataset list from the text file
lines = common_methods.dataset_paths()

#loop through the dataset list and get the file names for each dataset
#then add the file names to a clean list and record in a .txt
for line in lines:
    data_list_messy = api.dataset_list_files(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_list_clean = []
    for file in data_list_messy.files:
        data_list_clean.append(file.name)
    with open("dataset_file_list.csv", "a") as file:
        for name in data_list_clean:
            file.write(line + "," + name + "," + timestamp + "\n")