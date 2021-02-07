import numpy as np
import matplotlib.pyplot as plt

def create_visual_map(inputmatrix):
    # get images for tiles
    unexplored=plt.imread('unexplored.png')
    obstacle=plt.imread('obstacle.png')
    free=plt.imread('free.png')

    # define codes for tile types
    codes={0:unexplored,1:free,2:obstacle}

    # get input shape
    h,w=np.shape(inputmatrix)
    # initialize image for concat (zero height)
    image=np.empty((0,40*w,4))
    for row in inputmatrix:
        # initialize row for concat (zero width)
        newrow=np.empty((40,0,4))
        for element in row:
            # concat images of this row
            newrow = np.concatenate((newrow,codes[element]),axis=1)
        # concat the rows to form image
        image = np.concatenate((image,newrow),axis=0)
    return image