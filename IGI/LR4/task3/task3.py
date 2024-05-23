import statistics
import math
import matplotlib.pyplot as plt
import numpy as np


class XValuesClass:
    def __init__(self):
        self.x_values = np.arange(1.1, 10, 0.1)


class Series(XValuesClass):
    def __init__(self):
        super().__init__()
        self.eps = 1e-1

    def calculate_series(self):
        y_vals = []
        result = 0.0
        i = 0
        for x in self.x_values:
            while i <= 500:
                term = 2 / ((2 * i + 1) * (x ** (2 * i + 1)))
                if abs(term) < self.eps:
                    break
                result += term
                i += 1
            i = 0
            y_vals.append(result)
            result = 0.0
        return y_vals

    def calculate_math_series(self):
        y_vals = []
        for x in self.x_values:
            y_vals.append(math.log((x + 1) / (x - 1), math.e))
        return y_vals


class SeriesPlot(XValuesClass):
    def __init__(self, y_values, y_math_values):
        super().__init__()
        self.y_vals = y_values
        self.y_math_vals = y_math_values

    def build_plots(self):
        plt.plot(self.x_values, self.y_vals, label='My series', color='red')
        plt.plot(self.x_values, self.y_math_vals, label='Math series', color='green')

        plt.annotate('Mode', xy=(2.714043486548638, 0.8), xytext=(4, 2), arrowprops=dict(arrowstyle='->'))
        plt.legend()

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Series plot')
        plt.savefig('D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task3//functions.png')
        plt.show()


def task3_run():
    a = Series()
    y = a.calculate_series()
    print(f"Mean: {statistics.mean(y)}\n"
          f"Median: {statistics.median(y)}\n"
          f"Dispersion: {statistics.variance(y)}\n"
          f"MSE: {statistics.stdev(y)}\n"
          f"Mode: {statistics.mode(y)}")

    y_math = a.calculate_math_series()

    plot = SeriesPlot(y, y_math)
    plot.build_plots()
