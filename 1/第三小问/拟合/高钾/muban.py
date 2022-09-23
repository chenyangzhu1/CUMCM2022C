from pylab import *

from scipy.optimize import curve_fit

from scipy import stats


def func(x, a, b, c):
    return a * np.exp(b * x) + c


'''Exponential 3-param function.'''


# Read data.

x, y = np.loadtxt('exponential_data.dat', unpack=True)

# Define confidence interval.

ci = 0.95

# Convert to percentile point of the normal distribution.

# See: https://en.wikipedia.org/wiki/Standard_score
#
# pp = (1. + ci) / 2.
#
# # Convert to number of standard deviations.
#
# nstd = stats.norm.ppf(pp)
#
# print
# nstd

# Find best fit.

popt, pcov = curve_fit(func, x, y)

# Standard deviation errors on the parameters.

perr = np.sqrt(np.diag(pcov))

# Add nstd standard deviations to parameters to obtain the upper confidence

# interval.

popt_up = popt + nstd * perr

popt_dw = popt - nstd * perr

# Plot data and best fit curve.

scatter(x, y)

x = linspace(11, 23, 100)

plot(x, func(x, *popt), c='g', lw=2.)

plot(x, func(x, *popt_up), c='r', lw=2.)

plot(x, func(x, *popt_dw), c='r', lw=2.)

text(12, 0.5, '{}% confidence interval'.format(ci * 100.))

show()
