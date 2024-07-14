# ~/.kaggle/kaggle.json
# /kaggle.json

import kaggle
from urllib.parse import urlparse

kaggle.api.authenticate()

def url_converter():
    url = input('Enter dataset url: ')
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.strip('/').split('/')
    
    if len(path_segments) >= 3:
        username = path_segments[-2]
        dataset_name = path_segments[-1]
        print(f"{username}/{dataset_name}")
        return f"{username}/{dataset_name}"
    else:
        return None
    
def list_dataset_files():
    dataset_files = kaggle.api.dataset_list_files(dataset).files
    print(dataset_files)
    return dataset_files

def download_dataset():
    return kaggle.api.dataset_download_files(dataset, path='./data', unzip=True)

def get_metadata():
    return kaggle.api.dataset_metadata(dataset,path='./data')





dataset = url_converter()

list_dataset_files()

download_dataset()

get_metadata()
# kaggle.api.dataset_metadata(dataset,path='./data')
