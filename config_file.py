import numpy as np
import matplotlib.pyplot as plt

# Paths

main_path = "/home/thanatos/Todo/Imagenes/"
FF_path = "/home/thanatos/Todo/Imagenes/FF/"
RAW_path = "/home/thanatos/Todo/Imagenes/RAW/"


# Kernels

kernel_hc, div_hc, bias_hc = np.array([[-1.0,-1.0,-1.0],[-1.0,8.0,-1.0],[-1.0,-1.0,-1.0]]), 1.0, 0.0

# Segmentation

size_segmentation = 256
file_segmentation_FF = "FF_PMMA_28kV.txt"
file_segmentation_RAW = "RAW28kV.txt"
prefix_FF = "FF"
prefix_RAW = "RAW"

# Graph images 

color_map = "Greys_r"
dosis = ["1.76 mGy", "2.09 mGy", "2.52 mGy", "2.95 mGy", "3.36 mGy", "3.79 mGy"]

"""
plt.imshow(stack_RAW[0], cmap = color_map)
plt.colorbar()
plt.savefig("RAW_0.png")
plt.title("Imagen cruda 1")
plt.xlabel("Pixeles en x")
plt.ylabel("Pixeles en y")
plt.clf()

plt.imshow(stack_RAW[1], cmap = color_map)
plt.colorbar()
plt.savefig("RAW_1.png")
plt.title("Imagen cruda 2")
plt.xlabel("Pixeles en x")
plt.ylabel("Pixeles en y")
plt.clf()

plt.imshow(stack_RAW[2], cmap = color_map)
plt.colorbar()
plt.savefig("RAW_2.png")
plt.title("Imagen cruda 3")
plt.xlabel("Pixeles en x")
plt.ylabel("Pixeles en y")
plt.clf()
"""