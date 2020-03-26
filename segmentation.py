import numpy as np
import matplotlib.pyplot as plt
import config_file as cfg

#Creates a directory in "mypath"
def mkdir_p(mypath):

    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise


def segment(mypath,name,size,prefix):
    matrix_total = np.genfromtxt(name)
    rows_total = len(matrix_total)
    columns_total = len(matrix_total[0]) 
    images = []
    number_of_images = rows_total/size
    digits = len(str(abs(int(number_of_images))))
    for i in range(int(number_of_images)):
        images.append(matrix_total[int(size*i):int(size*(i+1)),:])
        np.savetxt(mypath + prefix +"_" + str(i).zfill(digits)+".txt",images[i])
