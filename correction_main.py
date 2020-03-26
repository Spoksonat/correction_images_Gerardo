import numpy as np
import matplotlib.pyplot as plt
import os
import config_file as cfg
import segmentation as sg
import hcpixels as hc
import randpixels as rnd
import calibration_FF_RAW as clb 
import save_images as sv

# If all the images are in one .txt, then the text file is segmented in its components
#sg.segment(cfg.FF_path,cfg.file_segmentation_FF,cfg.size_segmentation,cfg.prefix_FF)
#sg.segment(cfg.RAW_path,cfg.file_segmentation_RAW,cfg.size_segmentation,cfg.prefix_RAW)

# Load the name of all the files in FF path and RAW path respectively
all_in_FF, all_in_RAW = os.listdir(cfg.FF_path), os.listdir(cfg.RAW_path)
# Takes only the name of the txt files in FF path and RAW path respectively
all_FF_txt, all_RAW_txt = filter(lambda x: x[-4:] == ".txt",all_in_FF), filter(lambda x: x[-4:] == ".txt",all_in_RAW)
# Load the FF images (matrices) in an array (vector) called stack_FF and the RAW images in an array (vector) called stack_RAW  
stack_FF, stack_RAW = np.array([np.genfromtxt(cfg.FF_path+i).T for i in all_FF_txt]), np.array([np.genfromtxt(cfg.RAW_path+j).T for j in all_RAW_txt])

stack_FF = stack_FF

stack_FF, stack_RAW = hc.correction_zeros(stack_FF, stack_RAW)
stack_FF, stack_RAW = hc.correction_hc(stack_FF, stack_RAW)
stack_FF, stack_RAW = rnd.obtain_mu_sigma(stack_FF, stack_RAW)
stack_CORR = clb.calibration_frames_corr(stack_FF,stack_RAW)
sv.save_images_corr(stack_CORR)





