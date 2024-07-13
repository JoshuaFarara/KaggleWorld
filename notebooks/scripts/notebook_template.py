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
                    "Collection Me",
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
                        "# this is for jupyter notebook to show the plot in the notebook itself instead of opening a new window\n",
                        "%matplotlib inline"
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
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Set the option to show maximum columns"
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
                    "source": []
            }
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
