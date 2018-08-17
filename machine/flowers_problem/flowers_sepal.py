from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris


# Initialize the flowers data from sklearn library
def initialize_data():
    # charge data from datasets from sklearn about iris flowers
    iris_data = load_iris()
    # features data about the flowers ex.: [5.4 3 2 0.4]
    features = iris_data.data
    # flowers features names, ex.: sepal length
    features_names = iris_data.feature_names
    # targets of the data
    target = iris_data.target
    # name of the flowers
    target_names = iris_data.target_names

    return features, target, target_names


# Plotting the data from Setosa, Virginica and Versicolor flowers
def plotting_datas(features, target, range_value=3):

    # Defining the marker for each flower and plotting it
    for threshold in range(range_value):
        if threshold == 0:
            c = 'r'
            marker = '>'
        elif threshold == 1:
            c = 'g'
            marker = 'o'
        elif threshold == 2:
            c = 'b'
            marker = 'x'
        plt.scatter(features[target == threshold, 0],
                    features[target == threshold, 1],
                    marker=marker,
                    c=c)
    plt.legend(["Setosa", "Versicolor", "Virginica"], loc="best")
    plt.show()


# Getting the best accuracy to each feature
def get_accuracy(features):

    is_virginica = (labels == 'virginica')
    # Initialize best_acc to impossibly low value
    best_accuracy = -1.0
    best_feature = features[:, 1]
    best_threshold = features[:, 1]
    best_reverse = False

    for fi in range(features.shape[1]):

        # We are going to test all possible thresholds
        thresholds = features[:, fi]

        for threshold in thresholds:

            # Get the vector for feature `fi`
            feature_i = features[:, fi]

            # apply threshold `t`
            prediction = (feature_i > threshold)
            accuracy = (prediction == is_virginica).mean()
            reverse_accuracy = (prediction == ~is_virginica).mean()

            if reverse_accuracy > accuracy:
                reverse = True
                accuracy = reverse_accuracy
            else:
                reverse = False

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_feature = fi
                best_threshold = threshold
                best_reverse = reverse

    return best_accuracy, best_reverse, best_feature, best_threshold


# Verify if the sample is a virginica flower
def is_virginica_test(feature, threshold, reverse, example):
    "Apply threshold model to a new example"
    test = example[feature] > threshold
    if reverse:
        test = not test
    return test


if __name__ == '__main__':

    features, target, target_names = initialize_data()

    # seeing how many is setosa and non setosa
    labels = target_names[target]
    petal_length = features[:, 2]
    is_setosa = (labels == 'setosa')
    max_setosa = petal_length[is_setosa].max()
    min_non_setosa = petal_length[~is_setosa].min()
    max_non_setosa = petal_length[~is_setosa].max()

    print("Amount of Setosa Flowers =", max_setosa)
    print("Minimun of Non Setosa Flowers =", min_non_setosa)
    print("Amount of Non Setosa Flowers =", max_non_setosa)

    non_setosa_features = features[~is_setosa]
    non_setosa_target = target[~is_setosa]
    labels = labels[~is_setosa]

    best_accuracy, best_reverse, best_feature, best_threshold = get_accuracy(non_setosa_features)
    print("Accuracy = ", best_accuracy)
    print("Reverse = ", best_reverse)
    print("Feature = ", best_feature)
    print("Threshold = ", best_threshold)

    plotting_datas(features, target)

    result = is_virginica_test(best_feature, best_threshold, best_reverse, features)

    print("\n\nResult = ", result)