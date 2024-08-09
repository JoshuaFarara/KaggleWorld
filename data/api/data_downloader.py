# ~/.kaggle/kaggle.json
# /kaggle.json

import kaggle
from urllib.parse import urlparse
import os

kaggle.api.authenticate()

class Dataset:

    def __init__(self):
        # self.dataset = dataset
        self.folder_path  = "./data"
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def url_converter(self):
        url = input('Enter dataset url: ')
        parsed_url = urlparse(url)
        path_segments = parsed_url.path.strip('/').split('/')
        
        if len(path_segments) >= 3:
            username = path_segments[-2]
            dataset_name = path_segments[-1]
            self.dataset = username + '/' + dataset_name
            # print(f"{username}/{dataset_name}")
            print(self.dataset)
            return self.dataset
        else:
            return None
        
    def list_dataset_files(self):
        dataset_files = kaggle.api.dataset_list_files(self.dataset).files
        print(dataset_files)
        return dataset_files

    def download_dataset(self):
        return kaggle.api.dataset_download_files(self.dataset, self.folder_path, unzip=True)

    def get_metadata(self):
        return kaggle.api.dataset_metadata(self.dataset, self.folder_path)



dataset = Dataset() 
dataset.url_converter()
dataset.list_dataset_files()
dataset.download_dataset()
dataset.get_metadata()
# kaggle.api.dataset_metadata(dataset,path='./data')
