import numpy as np
from matplotlib import pyplot as plt

w = np.ones(51)
W = np.fft.fftshift(np.fft.fft(w,1024))

plt.plot(20*np.log10(np.absolute(W)/max(np.absolute(W))))
plt.title("Frequency response of rectangular window")
plt.show()