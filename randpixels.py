import numpy as np
import matplotlib.pyplot as plt
import config_file as cfg

def obtain_mu_sigma(stack_FF,stack_RAW):
    mu_FF, mu_RAW = np.mean(stack_FF), np.mean(stack_RAW)
    sigma_FF, sigma_RAW = np.std(stack_FF), np.std(stack_RAW)
    mask_FF, mask_RAW = [], []
    invert_mask_FF, invert_mask_RAW = [], []
    for im in stack_FF:
        diff_FF = np.abs(mu_FF - im)
        mask_FF_im= (diff_FF<4*sigma_FF).astype(float) 
        mask_FF.append(mask_FF_im)
        invert_mask_FF.append(1.0-mask_FF_im)
    for im in stack_RAW:
        diff_RAW = np.abs(mu_RAW - im)
        mask_RAW_im = (diff_RAW<4*sigma_RAW).astype(float) 
        mask_RAW.append(mask_RAW_im)
        invert_mask_RAW.append(1.0-mask_RAW_im)

    mask_FF, mask_RAW, invert_mask_FF, invert_mask_RAW = np.array(mask_FF), np.array(mask_RAW), np.array(invert_mask_FF), np.array(invert_mask_RAW)
    stack_FF_without_random, stack_RAW_without_random = stack_FF*mask_FF, stack_RAW*mask_RAW
    stack_FF_corr, stack_RAW_corr = stack_FF_without_random + mu_FF*invert_mask_FF, stack_RAW_without_random + mu_RAW*invert_mask_RAW

    return stack_FF_corr, stack_RAW_corr
