""" Figure with simple regression line """

# author: Thomas Haslwanter, date: Nov-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# additional packages
import sys
sys.path.append(os.path.join('.', '..', 'Quantlets', 'Utilities'))
import ISP_mystyle

# Generate the data
x = np.arange(-20, 80)
y = 10 + 0.2*x + 4*np.random.randn(len(x))

# Make the plot
sns.set_style('ticks')
sns.set_context('poster')
ISP_mystyle.set()

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x,y,'.')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

sns.despine()

# Draw the fitted line
p = np.polyfit(x,y, 1)
yFit = np.polyval(p, x)
ax.plot(x,yFit, 'r')

# Save and show
outFile = 'Linear_regression.png'
ISP_mystyle.printout_plain(outFile)