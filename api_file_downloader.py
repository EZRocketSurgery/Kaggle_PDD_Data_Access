import common_methods
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

lines = common_methods.dataset_paths()

for line in lines:
    api.dataset_download_files(line, path="datasets", unzip=True)