'''Sketch to indicate why the sample SD underestimates the population SD '''

# author: Thomas Haslwanter, date: Nov-2015

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import sys
sys.path.append(os.path.join('.', '..', 'Quantlets', 'Utilities'))
import ISP_mystyle

# Set up the three axes
fig, axs = plt.subplots(3,1)

# Data for the "wide" distribution
x_wide = np.linspace(-10,10,201)
gauss_wide = stats.norm(0,3).pdf(x_wide)

# Points for the narrow distribution
data = np.array([-1,1])

# On each of the three plots, plot a normal distribution fitted to the (two) datapoints:
for index, offset in enumerate([-3,0,3]):
    curData = data + offset
    fitPars = stats.norm.fit(curData)
    axs[index].plot(x_wide, gauss_wide, color='r', lw=2, ls='--')
    axs[index].plot(curData, 0.005+np.zeros_like(curData), 'bo')
    axs[index].plot(x_wide, stats.norm(*fitPars).pdf(x_wide))
    axs[index].set_yticks([])

# Save and show
outFile = 'fig_SDunderestimation.png'
ISP_mystyle.printout_plain(outFile)
