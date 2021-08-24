import matplotlib.pyplot as plt
import numpy as np


def one_value_per_label(title, Y_label, labels, values, X_label='', width=0.35):
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values, width)
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()


def two_value_per_label(title, Y_label, labels, values_I, values_II, sub_labels=("Kobiety", "Mężczyżni"), X_label='',
                        width=0.35):
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values_I, width, label=sub_labels[0])
    rects2 = ax.bar(x + width / 2, values_II, width, label=sub_labels[1])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


# not working now
def many_values_per_label(title, Y_label, labels, Values, sub_labels, X_label='', width=0.35):
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects = [ax.bar(x + width / len(sub_labels), Values[i], width, label=sub_labels[i]) for i in range(len(Values))]

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    for react in rects:
        ax.bar_label(react, padding=3)
    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    one_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15])
    two_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15], [10, 20, 25])
    sub_labels = [x for x in range(10)]
    Values = [[x for x in range(0, 100, 5)] for _ in range(5)]
    labels = [x for x in range(5)]
    print(Values)
    many_values_per_label("Nazwa", "wartości",labels,Values,sub_labels)
