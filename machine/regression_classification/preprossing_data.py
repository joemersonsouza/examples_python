import numpy as np
from sklearn import preprocessing

if __name__ == '__main__':

    input_data = np.array([[5.1, -2.9, 3.3],
                          [-1.2, 7.8, -6.1],
                          [3.9, 0.4, 2.1],
                          [7.3, -9.9, -4.5]])

    print("Default data")
    print(input_data)

    # Binarize data, transform the data into a boolean values
    # thresold is the limit of transform data
    data_binarized = preprocessing.Binarizer(threshold=0).transform(input_data)
    print("\nBinarize data")
    print(data_binarized)

    # Mean data, remove the mean from our feature vector and the mean value is very close to zero
    # Mean, before the standard deviation
    print("\nBefore Mean:")
    print("Mean =", input_data.mean(axis=0))
    print("Std deviation =", input_data.std(axis=0))

    # Mean, after the standard deviation
    data_scaled = preprocessing.scale(input_data)
    print("\nAfter Mean:")
    print("Mean =", data_scaled.mean(axis=0))
    print("Std deviation =", data_scaled.std(axis=0))

    # Scalling, is used to get random min and max value until a fixed value
    data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
    data_scaled = data_scaler.fit_transform(input_data)
    print("\nMin and Max Scaling")
    print(data_scaled)

    # Normalize data
    data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
    data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
    print("\nL1 normalized data:\n", data_normalized_l1)
    print("\nL2 normalized data:\n", data_normalized_l2)