import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

import click

def covariance_matrix(matrix):
    # the columns are each of the measurement types
    # rows are each of the measurements

    
    # take the mean along the columns for each of the measurement types
    normalized_matrix = (matrix - np.mean(matrix)).T 
    
    # compute the covariance matrix
    covariance_matrix = np.matmul(normalized_matrix, normalized_matrix.T) / (normalized_matrix.shape[0]-1)
    return covariance_matrix
    
def slice_eigen(color_matrix, num_components):
    
    # solve for the eigenvectors and eigenvalues
    evalues, evectors = np.linalg.eigh(covariance_matrix(color_matrix))
    if (num_components > len(evalues)):
        num_components = len(evalues)
        
    # slice the desired principal components
    desired_index = np.argsort(evalues)[::-1][:num_components]
    sorted_evalues = evalues[desired_index]
    sorted_evectors = evectors[:,desired_index]
    return sorted_evalues, sorted_evectors
    
def build_color_matrix(color_matrix, num_components):
    reval, revectors = slice_eigen(color_matrix, num_components)
    
    # compute the projection
    res = np.dot(revectors.T, (color_matrix - np.mean(color_matrix)).T)
    resul = np.dot(revectors, res)
    
    # need to reverse normalize the color_matrix so that it is centered on the mean of the original matrix
    resultt = (resul + np.mean(color_matrix)).T 
    
    # clean the data so that it is integers
    final = np.uint8(np.absolute(resultt)) 
    return final
    
def create_new_image(file_name, num_components):
    # read image data into a matrix
    raw = imread(file_name)
    
    # extract the RGB bytes
    r = raw[:, :, 0]
    g = raw[:, :, 1]
    b = raw[:, :, 2]
    
    # build each matrix using the functions defined above
    r_new = build_color_matrix(r, num_components)
    g_new = build_color_matrix(g, num_components)
    b_new = build_color_matrix(b, num_components)
    
    # stack the color matrices
    new_image = np.dstack((r_new, g_new, b_new))
    
    # new file name and saving the file
    new_file_name = file_name.split('.')[0] + '_result.' + file_name.split('.')[1]
    plt.imsave(new_file_name, new_image)
    
    
### THE CODE BELOW HAS NOTHING TO DO WITH PCA, FOR PARSING ARGUMENTS OF THE CLI TOOL

@click.command()
@click.argument('filename')
@click.argument('num_components')
def main(filename, num_components):
    click.echo("compressing image {} to {} principal components".format(filename, num_components))
    create_new_image(filename, int(num_components))
    new_file_name = filename.split('.')[0] + '_result.' + filename.split('.')[1]
    click.echo(f"image created! check for the {new_file_name} file in your current working directory")

if __name__ == "__main__":
    main()
