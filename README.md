# Principal Component Analysis with Applications to Image Compression

This project was created by Andrew Sima for Math22a: Vector Calculus and Linear Algebra, Fall2020. This accompanying repository includes an IPython Notebook and a CLI Tool to compress images of your choice. The annotated code containing the PCA algorithm can be found in `compress.py` or `pca_image_compression_test.ipynb` files.

To run the IPython Notebook, reference the docs [here](https://jupyter.readthedocs.io/en/latest/install/notebook-classic.html). The following instructions are for using the CLI Tool.

## Installation (CLI Tool)

If you don't have `pip` installed, please see [here](https://pip.pypa.io/en/stable/installing/).

1. Open a new terminal in the project directory and run `pip install -r requirements.txt` 

## Usage (CLI Tool)

1. Place the original image in the `test_files` folder.

2. To generate a new image from the principal components, run `python compress.py <filename> <number of components>`. The filename argument is just the filename, not the path in the directory (ex. to compress `test_files/cat.jpg` with `100` components, run `python compress.py cat.jpg 100`)
