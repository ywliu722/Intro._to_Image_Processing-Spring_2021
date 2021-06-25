import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def dft_2d(_img):
    # 2D DFT
    dft = cv.dft(np.float32(_img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # calculate magnitude
    magnitude = cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

    # do intensity transformation on magnitude
    magnitude_spe = (255 / np.log(1+np.amax(magnitude)))*np.log(1+magnitude)
    magnitude_spectrum = (255 / (255**2.5)) * (magnitude_spe ** 2.5)

    # plot Input Image
    plt.subplot(121), plt.imshow(_img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plot Magnitude Spectrum
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':

    # Load image
    img = cv.imread('Q4.tif', 0)

    # do DFT on img you loaded
    dft_2d(img)