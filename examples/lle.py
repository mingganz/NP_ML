import matplotlib.pyplot as plt
from sklearn import datasets
from np_ml import LLE

if __name__ == '__main__':
    lle = LLE()
    n_points = 1000
    X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
    
    y = lle.fit(X)
    plt.scatter(y[:, 0], y[:, 1], c=color)
    plt.show()