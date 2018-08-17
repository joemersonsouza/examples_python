import numpy as np
import argparse
import scipy as sp
import matplotlib.pyplot as plt

# Argument parser
def build_arg_parser():
    parser = argparse.ArgumentParser(description='Classify data using \
                     Ensemble Learning techniques')
    parser.add_argument('--degree', dest='degree',
                        required=True, choices=['1', '2', '3', '4'], help="Level of polynomial degree \
                        to use; can be either 1 to be lower until 4 to be highest")
    return parser


if __name__ == '__main__':

    args = build_arg_parser().parse_args()
    degree = args.degree

    data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
    x = data[:, 0]
    y = data[:, 1]

    # Getting amount of invalid data, other hand, the nan values
    invalid_data = sp.sum(sp.isnan(y))
    print("\nAmount of invalid values = ", invalid_data)

    # Removing nan values
    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

    polydeArray, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
    polyde = sp.poly1d(polydeArray)
    secondPolydeArray = sp.polyfit(x, y, 2)
    secondPolyde = sp.poly1d(secondPolydeArray)

    goodDegree = sp.polyfit(x, y, 40)
    goodPolyde = sp.poly1d(goodDegree)

    perfectDegree = sp.polyfit(x, y, 53)
    perfectPolyde = sp.poly1d(perfectDegree)

    # generate X-values for plotting
    fx = sp.linspace(0, x[-1], 1000)

    # calculate the inflection point in hours
    inflection = 3.5 * 7.0 * 24.0

    # data before the inflection point
    xa = x[:int(inflection)]
    ya = y[:int(inflection)]

    # data after
    xb = x[int(inflection):]
    yb = y[int(inflection):]

    fa = sp.poly1d(sp.polyfit(xa, ya, 1))
    fb = sp.poly1d(sp.polyfit(xb, yb, 1))

    # Plot the values with hour and amount of web request values
    plt.scatter(x, y, s=10)
    plt.title("We traffic per hour over the last month")
    plt.xlabel("Time")
    plt.ylabel("Requests")
    plt.xticks([w * 7 * 24 for w in range(10)],
               ['week %i' % w for w in range(10)])
    plt.autoscale(tight=True)

    if degree == '1':
        plt.plot(fx, polyde(fx), linewidth=2, color="red")
        plt.legend(["d=%i" % polyde.order],loc="upper left")
    elif degree == '2':
        plt.plot(fx, secondPolyde(fx), linewidth=2, color="red", linestyle='-')
        plt.legend(["d=%i" % secondPolyde.order],loc="upper left")
    elif degree == '3':
        plt.plot(fx, goodPolyde(fx), linewidth=2, color="red", linestyle='-')
        plt.legend(["d=%i" % goodPolyde.order],loc="upper left")
    elif degree == '4':
        plt.plot(fx, perfectPolyde(fx), linewidth=2, color="red", linestyle='-')
        plt.legend(["d=%i" % perfectPolyde.order],loc="upper left")

    # Plot inflection value
    plt.plot(fx, fb(fx), linewidth=2, color="green", linestyle='--')

    # Draw a slightly opaque, dashed grid
    plt.grid(True, linestyle='-.', color='gray')
    plt.show()
