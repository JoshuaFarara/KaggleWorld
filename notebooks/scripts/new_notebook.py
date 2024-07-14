'''
Generate a template Jupyter Notebook. 

user input of title

'''

import os
import json
from notebook_template import get_notebook_template


class Notebook:

    def __init__(self, notebook_title):
        self.notebook_title = notebook_title
        self.folder_path  = "./notebooks"
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)


    def generate_notebook(self):
        return get_notebook_template(self.notebook_title)
    
    def assign_dataset(self):
        dataset = input() 
        pass

    def get_title(self):
        print(f"Notebook title: {self.notebook_title}")

    def build_template(self):
        notebook_content = self.generate_notebook()

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