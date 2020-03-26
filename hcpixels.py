import numpy as np
import matplotlib.pyplot as plt
import config_file as cfg

def padding_image(image):
    rows,columns = len(image), len(image[0])
    padded_image = np.zeros((rows+2,columns+2))
    padded_image[1:-1,1:-1] = image
    padded_image[0,1:-1] = image[0,:]
    padded_image[-1,1:-1] = image[-1,:]
    padded_image[1:-1,0] = image[:,0]
    padded_image[1:-1,-1] = image[:,-1]
    padded_image[0,0] = image[0,0]
    padded_image[0,-1] = image[0,-1]
    padded_image[-1,0] = image[-1,0]
    padded_image[-1,-1] = image[-1,-1]
    return padded_image

def convolution(image,kernel,div,bias):
    padded_image = padding_image(image)
    rows, columns = len(padded_image), len(padded_image[0])
    new_image = np.zeros((rows,columns))
    d = len(kernel)-int((len(kernel)+1.0)/2.0) 
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            value_pixel = np.sum(padded_image[i-d:i+d+1,j-d:j+d+1]*kernel)/div + bias
            if(value_pixel > 0.2*np.amax(image)):
                new_image[i,j] = 1.0
            else:
                new_image[i,j] = 0.0
    return new_image[1:-1,1:-1]


def productory(array_of_images):
    image = np.ones((len(array_of_images[0]),len(array_of_images[0][0])))
    for i in array_of_images:
        image = image*i
    return image

def value_in_image(image,value):
    index_i = []
    index_j = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            if(image[i,j] == value):
                index_i.append(i)
                index_j.append(j)
    return index_i,index_j


def correction_hpixels(image):
    image = convolution(image,cfg.kernel_hc,cfg.div_hc,cfg.bias_hc)
    return image

def correction_cpixels(image):
    image = convolution(image,-cfg.kernel_hc,cfg.div_hc,cfg.bias_hc)
    return image

def correction_hc(stack_FF, stack_RAW):
    # Apply the filter to find the masks (matrices of 0's and 1's) for hot and cold pixels for every RAW image and every mask is saved in an array (one array for hot pixels and one array for cold pixels)
    stack_RAW_mask_hot, stack_RAW_mask_cold = np.array([correction_hpixels(j) for j in stack_RAW]), np.array([correction_cpixels(j) for j in stack_RAW])
    # The final mask is the product of all the mask in the mask array (mask_1 AND mask_2 AND ...).
    mask_hot, mask_cold = productory(stack_RAW_mask_hot), productory(stack_RAW_mask_cold)

    # Find the positions in the mask where there is a 1 (find the place where there is a hot or cold pixel)
    index_mask_hot_i, index_mask_hot_j = value_in_image(mask_hot,1.0)
    index_mask_cold_i, index_mask_cold_j= value_in_image(mask_cold,1.0)

    # The value of the hot or cold pixel is replaced by the mean value of the image     
    for j in stack_RAW:
        j[index_mask_hot_i, index_mask_hot_j] = np.mean(j)
        j[index_mask_cold_i, index_mask_cold_j] = np.mean(j)

    for j in stack_FF:
        j[index_mask_hot_i, index_mask_hot_j] = np.mean(j)
        j[index_mask_cold_i, index_mask_cold_j] = np.mean(j)
    
    return stack_FF, stack_RAW


def correction_zeros(stack_FF,stack_RAW):

    for j in stack_FF:
        index_i,index_j = value_in_image(j,0.0)
        j[index_i, index_j] = np.mean(j)

    for j in stack_RAW:
        index_i,index_j = value_in_image(j,0.0)
        j[index_i, index_j] = np.mean(j)

    return stack_FF, stack_RAW

    
    