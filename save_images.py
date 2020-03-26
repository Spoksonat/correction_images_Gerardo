import numpy as np
import matplotlib.pyplot as plt
import config_file as cfg

def save_images_corr(stack_corr):
    i = 0
    for image in stack_corr:
        plt.imshow(image, cmap = cfg.color_map)
        cbar = plt.colorbar()
        cbar.set_label("FF/RAW")
        plt.savefig("Corr" + cfg.dosis[i] + ".png")
        plt.title("Fantoma I - CORR a " + cfg.dosis[i])
        plt.xlabel("Pixeles en x")
        plt.ylabel("Pixeles en y")
        plt.clf()
        i = i+1