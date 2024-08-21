'''
Generate a template Jupyter Notebook. 

user input of title

'''

import os
import sys
import json
from notebook_template import get_notebook_structure
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data.api.data_downloader import Dataset
# import ./api/data_downloader


class Notebook:

    def __init__(self, notebook_title):
        self.notebook_title = notebook_title
        self.folder_path  = "./notebooks"
        self.dataset = None

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)


    # def generate_notebook(self):
    #     return get_notebook_structure(self.notebook_title)
    
    def assign_dataset(self):
        #  Create Dataset object and download the dataset
        self.dataset = Dataset()
        self.dataset.url_converter()
        self.dataset.list_dataset_files()
        self.dataset.download_dataset()
        metadata = self.dataset.get_metadata()
        return metadata

    def get_title(self):
        print(f"Notebook title: {self.notebook_title}")

    def build_template(self):
        # notebook_content = self.generate_notebook()
        notebook_content = get_notebook_structure(self.notebook_title)

        sanitized_title = self.notebook_title.lower().replace(' ', '_')
        
        # Create the file path
        filepath = os.path.join(self.folder_path, f"{sanitized_title}.ipynb")
        
        # Write the notebook content to the file
        with open(filepath, 'w') as fp:
            json.dump(notebook_content, fp, indent=4)
        print(f"Notebook '{self.notebook_title}' has been created at {filepath}")

title = input('Enter a title of the notebook: ')
notebook = Notebook(title)
notebook.get_title()
notebook.build_template()