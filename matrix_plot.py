from __future__ import division
from matplotlib import pyplot as plt
import string
import numpy as np

def matrix_plot(img, figsize=(10, 10), charsize=15, sort=True,
                brighten=1.0, fade=0.7):
    '''
    Plot image in matrix style

    The iconic matrix background with the symbols is created
    and the image is used as a filter for this.
    
    Parameters
    ----------
    
    img : *.png
        Image that is to be shown; only brightness information
        is used, not colour channels.
        
    figsize : tuple of 2 ints (default=(10, 10))
        Figure size of the image.
        
    charsize : int (default=15)
        Size of the green characters, has to be adjusted to
        figure size.
        
    sort : bool (default=True)
        Whether symbols should be sorted in order of
        descending brightness; looks better IMO but choice
        is up to user.
        
    brighten : float (default=1.0)
        Parameter for brightening the image, higher means
        brighter.
        
    fade : float (default=0.7)
        Parameter that controls how strongly the brightness
        fades when moving down the image; higher means
        stronger fading.
        
    Result
    ------
    
    The final image

    '''

    # letters and digits used for plot
    letters = list(string.ascii_letters + string.digits)

    # normalize image
    img = (img - img.min()) / (img.max() - img.min())
    # brighten image, higher value -> lighter
    img = img ** brighten
    img = img.T
    s0, s1 = img.shape
    # offsets
    ox, oy = 1 / s0, 1 / s1

    # the actual matrix to be plotted
    mat = np.random.rand(s0, s1)
    mat = mat ** fade
    if sort:
        mat = np.fliplr(np.sort(mat, axis=1))
    # image serves as filter for matrix
    mat *= img

    fig, ax = plt.subplots(figsize=figsize)
    ax.set_axis_bgcolor('black')
    for i in range(s0):
        check = True
        for j in range(s1):
            char = np.random.choice(letters)
            plt.text(i * ox, 1 - (j + 1) * oy, char,
                     alpha=mat[i, j], fontsize=charsize,
                     color='#008800', fontdict={'weight':'bold'})
    plt.xticks([])
    plt.yticks([])
    plt.show()