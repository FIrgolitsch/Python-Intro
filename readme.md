## Python Introduction

This repository will contain notebooks to help get started with python and learn the fundamentals. It's split into the
following chapters which each have a notebook (Chapter 12-18 are still in development):

* Chapter 01: Introduction to Python
* Chapter 02: Python Data Types
* Chapter 03: Python Operators
* Chapter 04: Python Collections
* Chapter 05: Python Flow Control
* Chapter 06: Python Functions
* Chapter 07: Python Classes
* Chapter 08: Python Modules & Packages
* Chapter 09: Python File I/O
* Chapter 10: Python Exceptions
* Chapter 11: Python Libraries
* Chapter 12: NumPy
* Chapter 13: Pandas
* Chapter 14: Matplotlib
* Chapter 15: SciPy
* Chapter 16: Dask
* Chapter 17: Neuroimaging in Python
* Chapter 18: Neuroinformatics in Python

### Getting Started

To get started, you'll need to have Python installed on your machine. You can download it from
the [official website](https://www.python.org/downloads/). For better environment management, you can use Anaconda which
you can download from [here](https://www.anaconda.com/products/individual). Miniconda is also a good option if you want
a lightweight version of Anaconda which you can download from [here](https://docs.conda.io/en/latest/miniconda.html).
The author of this repository uses and recommends Miniconda.

### Running the Notebooks

To run the notebooks, you'll need to have Jupyter installed. You can set up a minimal environment by running the
following commands (with Anaconda or Miniconda installed) in a terminal (MacOs/Linux) or command prompt (Windows):

```bash
# This will create a new environment called python-intro with Python 3.10 and Jupyter installed
conda create -n python-intro python=3.10 jupyter

# This will activate the environment
conda activate python-intro

# This will install the required packages (run this in the root folder of the repository)
pip install -r requirements.txt

# This will start Jupyter
jupyter lab
```

This will open a new tab in your browser where you can navigate to the notebooks and run them. Make sure to run these
commands in the root folder of the repository. The folder where you run the `juptyer lab` command will be the root
folder in the notebook server that will start so you can navigate to the notebooks from there.
