import numpy as np
import matplotlib.pyplot as plt
import config_file as cfg

def calibration_frames_corr(stack_FF,stack_RAW):
    RAW_40mAs = np.sum(stack_RAW[:41],axis=0) # sum from image 0 to 40 (sum of 41 images)
    RAW_50mAs = np.sum(stack_RAW[:52],axis=0) # sum from image 0 to 51 (sum of 52 images)
    RAW_60mAs = np.sum(stack_RAW[:62],axis=0) # sum from image 0 to 61 (sum of 62 images)
    RAW_70mAs = np.sum(stack_RAW[:73],axis=0) # sum from image 0 to 72 (sum of 73 images)
    RAW_80mAs = np.sum(stack_RAW[:83],axis=0) # sum from image 0 to 82 (sum of 83 images)
    RAW_90mAs = np.sum(stack_RAW[:93],axis=0) # sum from image 0 to 92 (sum of 93 images)
    im_FF = np.sum(stack_FF,axis=0)
    return np.array([im_FF/RAW_40mAs, im_FF/RAW_50mAs, im_FF/RAW_60mAs, im_FF/RAW_70mAs, im_FF/RAW_80mAs, im_FF/RAW_90mAs])