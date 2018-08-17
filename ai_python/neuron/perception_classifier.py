import numpy as np
# import matplotlib.pyplot as plt
import neurolab as nl

text = np.loadtxt('data_perceptron.txt')

data = text[:, :2]
labels = text[:, 2].reshape((text.shape[0], 1))

# plt.figure()
# plt.scatter(data[:,0], data[:,1])
# plt.xlabel('Dimension 1')
# plt.ylabel('Dimension 2')
# plt.title('Input')
#
# plt.show()

dim1_min, dim1_max, dim2_min, dim2_max = 5, 0, 23, 5

num_output = labels.shape[1]

dim1 = [dim1_min, dim1_max]
dim2 = [dim2_min, dim2_max]

perceptron = nl.net.newp([dim1, dim2], num_output)

error_progress = perceptron.train(data, labels, epochs=100, show=20, lr=0.03)

print(error_progress)

# plt.figure()
# plt.scatter(error_progress)
# plt.xlabel('Number of epochs 1')
# plt.ylabel('Training error')
# plt.title('Error progress')
#
# plt.show()
