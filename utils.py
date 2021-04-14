from matplotlib import pyplot as plt


def plot_c(c, alpha, threshold):
    c_list = [c]
    while c > threshold:
        c = c * alpha
        c_list.append(c)
    plt.plot(c_list)
    plt.show()
