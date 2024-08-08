def get_notebook_structure(notebook_title):
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {notebook_title}\n",
                    "![image_name](./assets/image_name.png \"alt-image_name!\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## About Author\n", 

                    "Author: Joshua Farara\n",

                    f"Project: {notebook_title}\n",

                    "### Contact Info\n",
                    "Click on link below to contact/follow/correct me:\n",
                    "\n",
                    "Email: joshua.farara@gmail.com\n",
                    "\n",
                    "[LinkedIn](https://www.linkedin.com/in/joshuafarara/)\n",
                    "\n",
                    "[Facebook](https://www.facebook.com/josh.farara/)\n",
                    "\n",
                    "[Twitter](https://x.com/FararaTheArtist)\n",
                    "\n",
                    "[Github](https://github.com/JoshuaFarara)\n"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## About Data\n",
                    "\n",
                    "Title: Dataset Title\n",
                    "\n",
                    "Dataset: Link\n",
                    "\n",
                    "Brief Description of dataset\n",
                    "\n",
                    "### Dataset Columns Names\n",
                    "\n",
                    "Features:\n",
                    "\n",
                    "### Metadata\n",
                    "\n",
                    "Source:\n",
                    "Collection Methodology",
                    "\n",
                    "License:\n",
                    "### Task\n",
                    "Describe task\n",
                    "\n",
                    "### Objective\n",
                    "\n",
                    "Describe observed objective of dataset.\n",
                    "\n",
                    "### Kernel Version Used\n",
                    "\n",
                    "Python==3.11.7\n"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Import Libraries\n",
                    "We will use the following libraries\n",
                    "1. Pandas: Data manipulation and analysis\n",
                    "2. Numpy: Numerical operations and calculations\n",
                    "3. Matplotlib: Data visualization and plotting\n",
                    "4. Seaborn: Enhanced data visualization and statistical graphics\n",
                    "5. Scipy: Scientific computing and advanced mathematical operations\n",
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "import pandas as pd\n",
                        "import numpy as np\n",
                        "import matplotlib.pyplot as plt\n",
                        "import seaborn as sns\n",
                        "import scipy as sp\n",
                        "import os\n",
                        "import sys\n",
                        "# this is for jupyter notebook to show the plot in the notebook itself instead of opening a new window\n",
                        "%matplotlib inline"

                        "for dirname, _, filenames in os.walk('/kaggle/input'):"
                           "for filename in filenames:"
                               "print(os.path.join(dirname, filename))"

                        "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using " 
                        "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"   
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Data Loading and Exploration | Cleaning"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Load a CSV file then creating a dataframe"
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# Kaggle Notebook"
                        "# df = pd.read_csv('/kaggle/input/coffee-sales/index.csv')"
                        "# Local Machine Notebook"
                        "df = pd.read_csv('../../data/data.csv')"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Set the option to show maximum columns"
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "pd.set_option('display.max_columns', None) "
                        "pd.set_option('display.max_rows', None)"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Get a sneak peek of data\n",
                        "The purpose of a sneak peek is to get a quick overview of the data and identify any potential problems or areas of interest"
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "df.head(5)"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Let's see the column names"
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "df.columns"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Let's have a look on the shape of the dataset"
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "print(f\"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.\")"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Let's have a look on the columns and their data types using detailed info function"
                ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "df.info()"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Count the missing values"
                    ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "df.isnull().sum()"
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Cleaning Data"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### First Step of Cleaning"   
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Second Step of Cleaning"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Third Step of Cleaning"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Fourth Step of Cleaning"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Fifth Step of Cleaning"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Restructure dateframe order."
                    ]
            },
            {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# fill in restructureed dateframe format for desired look of data.  "
                ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Analytical Questions"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "Analysis Subject 1"
                        "1. "
                        "2. "
                        "3. "
                        "4. "
                        "5. "
                        "Analysis Subject 2"
                        "6. "
                        "7. "
                        "8. "
                        "9. "
                        "10. "
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Summary"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Contact Information"
                    ]
            },
            {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "Click on link below to contact/follow/correct me:\n",
                        "\n",
                        "Email: joshua.farara@gmail.com\n",
                        "\n",
                        "[LinkedIn](https://www.linkedin.com/in/joshuafarara/)\n",
                        "\n",
                        "[Facebook](https://www.facebook.com/josh.farara/)\n",
                        "\n",
                        "[Twitter](https://x.com/FararaTheArtist)\n",
                        "\n",
                        "[Github](https://github.com/JoshuaFarara)\n"
                ]
            },
        ],
        "metadata": {
        "kernelspec": {
        "display_name": "venv",
        "language": "python",
        "name": "python3"
        },
        "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.11.7"
        }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
