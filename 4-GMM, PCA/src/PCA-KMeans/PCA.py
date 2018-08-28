from __future__ import print_function

import os
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from scipy import misc
from struct import unpack

from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from numpy import *

def pca(x):
    """Performs principal component on x, a matrix with observations in the rows.
    Returns the projection matrix (the eigenvectors of x^T x, ordered with largest eigenvectors first) and the eigenvalues (ordered from largest to smallest).
    """
    
    x = (x - x.mean(axis = 0)) # Subtract the mean of column i from column i, in order to center the matrix.
    
    num_observations, num_dimensions = x.shape
    
    # Often, we have a large number of dimensions (say, 10,000) but a relatively small number of observations (say, 75). In this case, instead of directly computing the eigenvectors of x^T x (a 10,000 x 10,000 matrix), it's more efficient to compute the eigenvectors of x x^T and translate these into the eigenvectors of x^T x by using the transpose trick. 
    # The transpose trick says that if v is an eigenvector of M^T M, then Mv is an eigenvector of MM^T.
   
    if num_dimensions > 25:
        eigenvalues, eigenvectors = linalg.eigh(dot(x, x.T))
        v = (dot(x.T, eigenvectors).T)[::-1] # Unscaled, but the relative order is still correct.
        s = sqrt(eigenvalues)[::-1] # Unscaled, but the relative order is still correct.
    else:
        u, s, v = linalg.svd(x, full_matrices = False)
        
    return v, s

def main():

    dataset_train = np.zeros((50000,784))
    label_train = np.zeros(50000)
    dataset_test = np.zeros((10000,784))
    label_test = np.zeros(10000)

    train_name = './dataset/mnist_train.txt'
    test_name = './dataset/mnist_test.txt'

    fname = 'pca_test.txt'
    
    with open(fname,'w') as f:
        count = 0
        with open(test_name) as te:
            lines = [line.rstrip('\n') for line in open(test_name)]
            for line in lines:
                line = line.strip()
                header, line = line.split(':')
                header, digit = header.split()
                pixels = line.split()
                if(count < 10000):
                    for i in range(0,784):
                            dataset_test[count][i] = int(pixels[i])
                    label_test[count] = int(digit)
                count += 1

        pcaModel = PCA()
        pcaModel.fit(dataset_test)
        eigenValues = pcaModel.explained_variance_
        N_comp = 25

        result = PCA(n_components = N_comp)

        dataset_test = result.fit_transform(dataset_test)

        for i in range(0,np.shape(label_test)[0]):
            out_str = "digit "
            out_str += str(label_test[i]) + ':'
            for k in range(0,N_comp):
                out_str += str(dataset_test[i][k]) + " "
            out_str = out_str[:-1] + '\n'
            f.write(out_str)

    fname = 'pca_train.txt'
    with open(fname,'w') as f:
        count = 0
        # Load the dataset
        with open(train_name) as tr:
            lines = [line.rstrip('\n') for line in open(train_name)]
            for line in lines:
                line = line.strip()
                header, line = line.split(':')
                header, digit = header.split()
                pixels = line.split()
                if(count < 50000):
                    for i in range(0,784):
                            dataset_train[count][i] = int(pixels[i])
                    label_train[count] = int(digit)
                    count += 1
        
        pcaModel = PCA()
        pcaModel.fit(dataset_train)
        eigenValues = pcaModel.explained_variance_
        N_comp = 25

        result = PCA(n_components = N_comp)

        dataset_train = result.fit_transform(dataset_train)

        for i in range(0,np.shape(label_train)[0]):
            out_str = "digit "
            out_str += str(label_train[i]) + ':'
            for k in range(0,N_comp):
                out_str += str(dataset_train[i][k]) + " "
            out_str = out_str[:-1] + '\n'
            f.write(out_str)

if __name__ == '__main__':
    main()
