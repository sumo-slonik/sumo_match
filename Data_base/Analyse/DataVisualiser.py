import matplotlib.pyplot as plt
import numpy as np


def one_value_per_label(title, Y_label, labels, values, X_label='', width=0.35):
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values, width)
    ax.set_ylabel(Y_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    one_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15])
